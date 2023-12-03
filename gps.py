import gpsd

def main():
    gpsd.connect(host="localhost", port=2947)

    packet =gpsd.get_current()
    print(f"latitude: {packet.lat}, longitude: {packet.lon}")
    return packet.lat, packet.lon

if __name__ =='__main__':
    main()
