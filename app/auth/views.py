from flask_login import login_user, logout_user

from app.models import User
from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form = request.form
        username = form.get('username')
        password = form.get('password')
        print(username)
        user = User.query.filter_by(username=username).first()
        if user is None:
            error = 'A user with that username  does not exist'
            return render_template('login.html', error=error)
        is_correct_password = user.check_password(password)
        print(is_correct_password)
        if not is_correct_password:
            error = 'A user with that password does not exist'
            return render_template('login.html', error=error)
        login_user(user)
        return redirect('/')
    return render_template('login.html')