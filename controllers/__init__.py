from . import employee
from . import room
from . import event

routes = [
    employee.router,
    room.router,
    event.router
]