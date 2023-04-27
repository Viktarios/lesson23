from bus import Bus


class Manager:

    def find_bus(buses):
        if not isinstance(buses, (list, tuple)):
            return Bus()

        target = buses[0]

        for bus in buses:
            if isinstance(bus, Bus):
                if (bus._price / bus._number) < (target._price / target._number):
                    target = bus

        return target
