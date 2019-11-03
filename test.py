
from sonaWue import SonaWue
from config import credentials

# sona = SonaWue(username=credentials["username"], password=credentials["password"])
sona = SonaWue(token="")

# sona.test_connection()
# sona._login_page()
# sona.custom_icon()
# sona.my_schedule()
# sona.main_menu_info()
# sona.study_page_info()

sona.study_info(1588)