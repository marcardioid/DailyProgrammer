def draw_circuit(led_v, led_c, bat_v, bat_c, hours):
    led = "-|>|-"
    serial = int(bat_v / led_v)
    d, m = divmod(int(((bat_c / hours) / led_c) * serial), serial)
    print("Resistor: {:.3f} Ohms".format(hours * ((bat_v - (serial * led_v)) / (bat_c / 1000))))
    print("Scheme:")
    for i in range(0, d):
        s = '*' if i == 0 else ' '
        print("{}{}-{}".format(s, "--|>|-" * serial, s))
        if i < d - 1 or m > 0:
            print(" |{}|".format(' ' * ((6 * serial) - 1)))
    if m > 0:
        s = '*' if d == 0 else ' '
        print("{}-{}".format(s, "-|>|--" * m).ljust((6 * serial) + 2, '-') + s)

if __name__ == "__main__":
    draw_circuit(1.7, 20, 9, 1200, 20)