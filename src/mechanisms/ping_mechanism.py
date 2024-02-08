from ping3 import ping


def check_ping(server):
    try:
        response = ping(server)

        if response is not None:
            pv = round(response * 1000, 2)
            print(f"Ping {server}: {pv} ms")
            return pv
        else:
            return None

    except Exception as ex:
        print(f"Error during ping: {ex}")
        return None
