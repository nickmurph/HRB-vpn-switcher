from nordvpn_switcher import initialize_VPN, rotate_VPN
import time

# command line interface, allows you to pick from some preset choices
# won't flow with intended use-case in HRB project, but useful otherwise
# Instructions = initialize_VPN()



# Run once with save=1 to create or update settings_nordvpn.txt. Otherwise, use stored_settings=1 
# instructions = initialize_VPN(save=1,area_input=['complete rotation'])



# Call this function each time you need to swap your NordVPN server a single time (eg: in a loop, make 4-5 requests until blacklisted and then call this function)
# Note that with this configuration, the nordvpn-switcher library calls down a list of all ~5000 NordVPN servers worldwide and connects to one randomly
# This is not a speedy process, due to size of server list and dependencies upon the NordVPN desktop app, and will likely be the most obvious bottleneck in your code
def single_random_vpn_swap():
    instructions = initialize_VPN(stored_settings=1)
    rotate_VPN(instructions) 

# same as above but utilizing the library's captcha avoidance
def single_random_vpn_swap_captcha():
    instructions = initialize_VPN(stored_settings=1)
    rotate_VPN(instructions, google_check = 1) 

# Can use a country or region name as parameter for more exact approach (may have beneficial speed implications in future)
# see 
def single_targeted_vpn_swap(countryName):
    instructions = initialize_VPN(area_input=[countryName])
    rotate_VPN(instructions) 

# Same as above but with captcha avoidance
# see countrylist.txt for valid parameters
def single_targeted_vpn_swap_captcha(locationName):
    instructions = initialize_VPN(area_input=[locationName])
    rotate_VPN(instructions, google_check = 1) 





#single_random_vpn_swap()

# single_targeted_vpn_swap('United States')

#single_targeted_vpn_swap('North Macedonia')