# Duplicate Numbers

PASS

## Introduction

HELLO


## Test Cases

| Input        | Output         |
| ------------- |---------------|
| [1,1] | [1] |
| [1,2,3]    | [ ] |
| [1,1,2,2,2,3] | [1,2] |
| [ ] | [ ] |
| [2,1,2] | [2] |
| ["A String"] | [ ] | 
| ["A String", "A String"] | [ ] |
| [ True ] | [] |
| [ True, True ] | [ ]
| [1,1, True] | [1] |

## How to achive it

1. Take each element
2. Count number of that element
3. If greater then 1 place in an array and if int and if not already contained in output array

## Translate into code

1. For element in list :
2. if list.count(element) >= 2 && element is int && output.count < 1 
3. output.append(element)