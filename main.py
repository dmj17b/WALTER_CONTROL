import odrive

def main():
    odrv0 = odrive.find_any()
    print(str(odrv0.vbus_voltage))
    print("Hello, world!")


if __name__ == "__main__":
    main()