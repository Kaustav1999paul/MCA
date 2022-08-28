echo "Enter the first value: "
read a
echo "Enter the second value: "
read b

echo "arithmatic oprerator"
val=`expr $a + $b`
echo "a + b : $val"

val=`expr $a - $b`
echo "a - b : $val"

val=`expr $a \* $b`
echo "a * b : $val"

val=`expr $b / $a`
echo "b / a : $val"

val=`expr $b % $a`
echo "b % a : $val"

echo "Relational Operators"
if [ $a -eq $b ]
then 
	echo "both are equal"
else
	echo "not equal"
fi
if [ $a -gt $b ]
then 
	echo "a > b"
else
	echo "b > a"
fi

