from flask import Flask, render_template

app = Flask(__name__, static_folder="static", template_folder="templates", static_url_path="/")


@app.route('/')
def index():
    return render_template('index.html', arabic=False, other_version_url='/ar')


@app.route('/ar')
def index_ar():
    return render_template('index_AR.html', arabic=True, other_version_url='/')


@app.route('/about_us')
def about_us():
    return render_template('About_us.html', arabic=False, other_version_url='/about_us_ar')


@app.route('/about_us_ar')
def about_us_ar():
    return render_template('about_us_AR.html', arabic=True, other_version_url='/about_us')


@app.route('/our_services')
def our_services():
    return render_template('our_services.html', arabic=False, other_version_url='/our_services_ar')


@app.route('/our_services_ar')
def our_services_ar():
    return render_template('our_services_ar.html', arabic=True, other_version_url='/our_services')


@app.route('/our_projects')
def our_projects():
    return render_template('our_projects.html', arabic=False, other_version_url='/our_projects_ar')


@app.route('/our_projects_ar')
def our_projects_ar():
    return render_template('our_projects_ar.html', arabic=True, other_version_url='/our_projects')


@app.route('/Technologies_and_Systems')
def technologies_and_systems():
    return render_template('technologies_and_systems.html', arabic=False, other_version_url='/Technologies_and_Systems_ar')


@app.route('/Technologies_and_Systems_ar')
def technologies_and_systems_ar():
    return render_template('technologies_and_systems_ar.html', arabic=True, other_version_url='/Technologies_and_Systems')


@app.route('/Quality_and_Safety')
def quality_and_safety():
    return render_template('quality_and_safety.html', arabic=False, other_version_url='/Quality_and_Safety_ar')


@app.route('/Quality_and_Safety_ar')
def quality_and_safety_ar():
    return render_template('quality_and_safety_ar.html', arabic=True, other_version_url='/Quality_and_Safety')


@app.route('/Clients_and_Partners')
def clients_and_partners():
    return render_template('clients_and_partners.html', arabic=False, other_version_url='/Clients_and_Partners_ar')


@app.route('/Clients_and_Partners_ar')
def clients_and_partners_ar():
    return render_template('clients_and_partners_ar.html', arabic=True, other_version_url='/Clients_and_Partners')


if __name__ == '__main__':
    app.run(debug=True)
