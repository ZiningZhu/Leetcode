/**
 * @param {string} s
 * @return {number}
 */
 /*
 * Time: O(n * maxlength)
 */
var lengthOfLongestSubstring = function(s) {
    var noreplist = [];
    var maxlength = 0;
    for (var i = 0; i < s.length; i++) {
        var n = indexof(noreplist, s[i]);
        if (n != -1) {
            noreplist = noreplist.slice(n+1);
            noreplist.push(s[i]);
        } else {
            noreplist.push(s[i]);
            if (noreplist.length > maxlength)
                maxlength = noreplist.length;
        }
    }
    return maxlength;
};

function indexof(arr, k) {
    var loc = -1;
    for (var i = 0; i < arr.length; i++) {
        if (k == arr[i]) {
            loc = i;
        }
    }
    return loc;
}
