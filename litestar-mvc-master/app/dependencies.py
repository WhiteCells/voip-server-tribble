"""

"""

from litestar.di import Provide
from app.repositories import provide_dialplan_repository, provide_acc_repository, provide_client_repository
from app.services import provide_dialplan_service, provide_acc_service, provide_client_service
from app.utils.database.session import provide_db_session
from app.utils.redisclient.redisclient import provide_redis_client


dependencies = {
    "db_session": Provide(provide_db_session),
    "redisclient": Provide(provide_redis_client),

    # repository
    "acc_repository": Provide(provide_acc_repository),
    "dialplan_repository": Provide(provide_dialplan_repository),
    "client_repository": Provide(provide_client_repository),

    # service
    "acc_service": Provide(provide_acc_service),
    "dialplan_service": Provide(provide_dialplan_service),
    "client_service": Provide(provide_client_service),
}
