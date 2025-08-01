def encoder(text):
    result = text[0]
    count = 1
    for t in range(1, len(text)):
        if text[t] == text[t-1]:
            count += 1
        elif text[t] != text[t-1]:
            result += str(count) if count != 1 else ""
            result += text[t]
            count = 1

    result += str(count) if count != 1 else ""
    return result


## javascript:function encode(str) {
#   let result = "";
#   for (let i = 0; i < str.length; i++) {
#     let count = 1;
#     while (i < str.length && str[i] === str[i + 1]) {
#       count++;
#       i++;
#     }
#     result += `${str[i]}${count > 1 ? count : ""}`;
#   }
#   console.log(result);
#   return result;
# }