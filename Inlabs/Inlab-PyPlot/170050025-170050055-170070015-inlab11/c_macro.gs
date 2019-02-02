function MD5 (input) {
  var rawHash = Utilities.computeDigest(Utilities.DigestAlgorithm.MD5, input);
  var txtHash = '';
  for (i = 0; i < rawHash.length; i++) {
    var hashVal = rawHash[i];
    if (hashVal < 0) {
      hashVal += 256;
    }
    if (hashVal.toString(16).length == 1) {
      txtHash += '0';
    }
    txtHash += hashVal.toString(16);
  }
  return txtHash;
}

function fillingGcolumn() {
  var spreadsheet = SpreadsheetApp.getActive();
  spreadsheet.getRange('G2').activate();
  spreadsheet.getCurrentCell().setFormula('=MD5(D2)');
  spreadsheet.getActiveRange().autoFill(spreadsheet.getRange('G2:G126'), SpreadsheetApp.AutoFillSeries.DEFAULT_SERIES);
  spreadsheet.getRange('G2:G126').activate();
};

