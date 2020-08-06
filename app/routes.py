from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from datetime import datetime
from app import app, db
from app.forms import LoginForm, MapDropForm
from app.models import User, MapDrop

@app.route('/')
@login_required
def index():
    return redirect(url_for('user', username=current_user.username))

@app.route('/entry/map', methods=['GET', 'POST'])
@login_required
def entry():
    mapdrops = current_user.map_drops.order_by(MapDrop.time.desc()).limit(app.config['MAPDROPS_PER_PAGE']).all()
    form = MapDropForm()
    if form.validate_on_submit():
        if form.delete.data:
            last_md = mapdrops[0]
            db.session.delete(last_md)
            db.session.commit()
            return redirect(url_for('entry'))        
        else:
            map = gold_map = rouge = 0
            if form.m1g0r0.data:
                map = 1            
            elif form.m2g0r0.data:       
                map = 2
            elif form.m0g1r0.data:       
                gold_map = 1
            elif form.m1g1r0.data:       
                map = gold_map = 1
            elif form.m2g1r0.data:       
                map, gold_map = 2, 1
            elif form.m0g0r1.data:       
                rouge = 1
            elif form.m1g0r1.data:       
                map = rouge = 1
            elif form.m2g0r1.data:       
                map, rouge = 2, 1
            elif form.m0g1r1.data:       
                gold_map = rouge = 1
            elif form.m1g1r1.data:       
                map = gold_map = rouge = 1
            elif form.m2g1r1.data:       
                map, gold_map, rouge = 2, 1, 1
            run = current_user.map_drops.count() + 1
            md = MapDrop(map=map, gold_map=gold_map, rouge=rouge, player=current_user, run=run)
            db.session.add(md)
            db.session.commit()
            return redirect(url_for('entry'))
    return render_template('entry.html', title='Entry', mapdrops=mapdrops, form=form)

@app.route('/explore')
@login_required
def explore():
    page = request.args.get('page', 1, type=int)
    mapdrops = MapDrop.query.order_by(MapDrop.time.desc()).paginate(page, app.config['MAPDROPS_PER_PAGE'], False)
    next_url = prev_url = None
    if mapdrops.has_next:
        next_url = url_for('explore', page=mapdrops.next_num)
    if mapdrops.has_prev:
        prev_url = url_for('explore', page=mapdrops.prev_num)
    return render_template('entry.html', title='Explore', user_unknown=True, mapdrops=mapdrops.items, 
                            next_url=next_url, prev_url=prev_url)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            flash('User does not exist.')
            return redirect(url_for('login'))
        if not user.check_password(form.password.data):
            flash('Password does not exist.')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    maps = db.session.query(db.func.sum(MapDrop.map)).filter_by(user_id=user.id).scalar()
    gold_maps = db.session.query(db.func.sum(MapDrop.gold_map)).filter_by(user_id=user.id).scalar()
    rouges = db.session.query(db.func.sum(MapDrop.rouge)).filter_by(user_id=user.id).scalar()
    mapdrops = user.map_drops.order_by(MapDrop.time.desc()).paginate(page, app.config['MAPDROPS_PER_PAGE'], False)
    next_url = prev_url = None
    if mapdrops.has_next:
        next_url = url_for('user', username=user.username, page=mapdrops.next_num)
    if mapdrops.has_prev:
        prev_url = url_for('user', username=user.username, page=mapdrops.prev_num)
    return render_template('user.html', title='Profile', user=user, maps=maps, gold_maps=gold_maps, rouges=rouges,
                            mapdrops=mapdrops.items, next_url=next_url, prev_url=prev_url)

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
