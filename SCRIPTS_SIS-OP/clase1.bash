echo -n "Ingrese un año: "
read year

if [ $((year % 4)) -eq 0 ] && [ $((year % 4)) -ne 100 ] || [ $((year % 400)) -eq 400 ]; then
    echo "El año $year es bisiesto"
else
    echo "El año $year no es bisiesto"
fi