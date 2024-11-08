from flask_admin.contrib.sqla import ModelView

from app import db, admin
from app.models import User, Role, CustomerType, Room, Floor, Comment, Evaluation, Policy, Booking, PaymentMethod, Style, BookingDetail


class UserView(ModelView):
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    create_modal = True
    column_filters = ['citizen_id', 'address', 'email', 'username', 'phone_number', 'fullname']
    column_searchable_list = ['citizen_id', 'address', 'email', 'username', 'phone_number', 'fullname']


admin.add_view(UserView(User, db.session))

