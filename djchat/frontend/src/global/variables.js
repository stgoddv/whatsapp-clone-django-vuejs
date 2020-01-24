export const colorOffsets = {
  red: Math.floor(Math.random() * 256),
  green: Math.floor(Math.random() * 256),
  blue: Math.floor(Math.random() * 256)
};

export const getHash = function(input) {
  var hash = 0,
    len = input.length;
  for (var i = 0; i < len; i++) {
    hash = (hash << 5) - hash + input.charCodeAt(i);
    hash |= 0;
  }
  return hash;
};
