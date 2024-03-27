from flask_login import logout_user as flask_logout_user
from flask import request
from .sqla.models import LoginUserLog
import datetime
from .manager import BaseSecurityManager

class CustomLogoutUser(BaseSecurityManager):
    def custom_logout_user(self, user):
        login_log = LoginUserLog(user_id=user.id, addr=request.remote_addr)
        login_log.status = "logout"
        login_log.reason = f"User {user.username} logged out."
        self.appbuilder.session.add(login_log)
        self.appbuilder.session.commit()
        flask_logout_user()

