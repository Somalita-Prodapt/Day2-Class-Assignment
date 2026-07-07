echo "Enter marks for Subject 1: "
read s1

echo "Enter marks for Subject 2: "
read s2

echo "Enter marks for Subject 3: "
read s3

echo "Enter marks for Subject 4: "
read s4

echo "Enter marks for Subject 5: "
read s5

total=$((s1 + s2 + s3 + s4 + s5))
average=$((total / 5))

echo "Total Marks: $total"
echo "Average Marks: $average"

if [[ $average -ge 90 && $average -le 100 ]]; then
    echo "Grade A"
elif [[ $average -ge 75 && $average -le 89 ]]; then
    echo "Grade B"
elif [[ $average -ge 60 && $average -le 74 ]]; then
    echo "Grade C"
elif [[ $average -ge 50 && $average -le 59 ]]; then
    echo "Grade D"
else
    echo "Fail"
fi
