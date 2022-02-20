from vpn_switch_main import single_random_vpn_swap


totalNumFileRequests = 10000
numReqBeforeBan = 5
numPasses = totalNumFileRequests / numReqBeforeBan

for i in range(numPasses):
    #
    # code here conducts 5 file requests/downloads
    #
    single_random_vpn_swap()
    # IP has now swapped, will be clean for each passthrough of loop