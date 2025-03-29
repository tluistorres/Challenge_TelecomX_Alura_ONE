"""Este script mostra algumas regras da PEP 9."""
import datetime as dt

TEMPERATURE_SCALES = ("fahrenheit", "kelvin", "celsius")

class TemperatureConverter:
    pass

def convert_to_celsius(degrees, source="fahrenheit"):
    """Esta função converte graus Fahrenheit ou Kelvin em graus Celsius"""
    if source.lower() == "fahrenheit":
        return (degrees-32) * (5/9)
    elif source.lower() == "kelvin":
        return degrees - 273.15
    else:
        return f"Don't know how to convert from {source}"

celsius = convert_to_celsius(44, source="fahrenheit")
non_celsius_scales = TEMPERATURE_SCALES[:1]

print("Current time: " + dt.datetime.now().isoformat())
print(f"A temperatura em Celsius é: {celsius:.2f}ºC")


# O :.2f é um formato de saída que especifica:

# - :: separador entre o nome da variável e o formato.
# - .2: número de casas decimais
# - f: tipo de formato (float)

# Com isso, a saída será:

# A temperatura em Celsius é: 6.67ºC