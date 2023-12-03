// AOC Day 1 Part 2
var lines = document.querySelector("pre").innerText.split("\n");
function number(line) {
  var num1 = -1;
  var num2 = -1;
  for (let i = 0; i < line.length; i++) {
    if (!isNaN(parseInt(line[i]))) {
      if (num1 == -1) {
        num1 = parseInt(line[i]);
      } else {
        num2 = parseInt(line[i]);
      }
    }
  }
  if (num2 == -1) {
    return parseInt(`${num1}${num1}`);
  } else {
    return parseInt(`${num1}${num2}`);
  }
}
lines.map((x) => number(x)).reduce((a, b) => a + b, 0);

// AOC Day 1 Part 2
var lines = document.querySelector("pre").innerText.split("\n");

const map = new Map([
  ["1", 1],
  ["one", 1],
  ["2", 2],
  ["two", 2],
  ["3", 3],
  ["three", 3],
  ["4", 4],
  ["four", 4],
  ["5", 5],
  ["five", 5],
  ["6", 6],
  ["six", 6],
  ["7", 7],
  ["seven", 7],
  ["8", 8],
  ["eight", 8],
  ["9", 9],
  ["nine", 9],
]);

function number(line) {
  if (line.length == 0) return 0;
  var num1 = -1;
  var num2 = -1;
  for (let i = 0; i < line.length; i++) {
    if (map.has(line[i])) {
      if (num1 == -1) {
        num1 = map.get(line[i]);
      } else {
        num2 = map.get(line[i]);
      }
    } else {
      options = [
        line.substring(i, i + 3 > line.length ? line.length : i + 3),
        line.substring(i, i + 4 > line.length ? line.length : i + 4),
        line.substring(i, i + 5 > line.length ? line.length : i + 5),
      ].filter((value, index, array) => array.indexOf(value) === index);
      // console.log(options);
      options.forEach((option) => {
        if (map.has(option)) {
          if (num1 == -1) {
            num1 = map.get(option);
          } else {
            num2 = map.get(option);
          }
        }
      });
    }
  }
  // console.log(line, num1, num2);
  if (num1 == -1) return 0;
  else if (num2 == -1) return parseInt(`${num1}${num1}`);
  else return parseInt(`${num1}${num2}`);
}
lines.map((x) => number(x)).reduce((a, b) => a + b, 0);

// AOC Day 2 Part 1
