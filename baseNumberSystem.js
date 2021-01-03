const baseNumberSystem = (start, end, base) => {
    if (base < 2) return [];
    const arrayOfExponentialNumbers = [];
    for (let exponent = start; exponent <= end; exponent++) {
        arrayOfExponentialNumbers.push((base ** exponent).toLocaleString('en'));
    }
    arrayOfExponentialNumbers.unshift(`base ${base}:`);    
    return arrayOfExponentialNumbers;
};

console.log();
console.log(baseNumberSystem(0, 12, 2));
console.log(baseNumberSystem(0, 12, 3));
console.log(baseNumberSystem(0, 12, 5));