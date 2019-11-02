

from sonaWue import SonaWue
from config import credentials

sona = SonaWue(credentials["username"], credentials["password"])

# sona.test_connection()
# sona._login_page()
# sona._custom_icon()
sona._my_schedule()