const list1 = [1, 2, 3, 4, 5];

const list1reduced = list1.reduce((res, cur) => {
    return res + cur;
}, 0 )

console.log(list1reduced);