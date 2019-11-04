
from SonaWrap.Wrapper import SonaWrap
from config import credentials

sona = SonaWrap(username=credentials["username"], password=credentials["password"])
# sona = SonaWrap(token="b93ef8aed029418f871dc09c83283b67")

# sona.test_connection()
# sona._login_page()
# sona.custom_icon()
# sona.my_schedule()
# sona.main_menu_info()
# sona.study_page_info()

sona.study_info(1588)