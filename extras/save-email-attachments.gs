/**
 * Saves every document attachment (PDF, Word, Excel, PowerPoint, CSV) from your Gmail
 * (received AND sent) into the Drive folder "Reading now". Runs automatically every 10 minutes.
 *
 * Setup (about 2 minutes, once):
 * 1. Go to script.google.com while signed in as your work account, click New project.
 * 2. Delete the starter code, paste all of this in, click Save.
 * 3. Pick the function "setup" in the dropdown and click Run. Approve the Google permissions.
 *    (Gmail read + label, Drive create files.) setup() also backfills the last 30 days.
 * That's it. It only adds files to one Drive folder. It never sends, labels, deletes or archives anything. Duplicates are skipped by file name.
 */

var FOLDER_NAME = 'Reading now';
var DOC_TYPES = ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'csv', 'ppt', 'pptx'];

function setup() {
  ScriptApp.getProjectTriggers().forEach(function (t) { ScriptApp.deleteTrigger(t); });
  ScriptApp.newTrigger('saveNewAttachments').timeBased().everyMinutes(10).create();
  saveAttachments_('newer_than:30d');
}

function saveNewAttachments() {
  saveAttachments_('newer_than:2d');
}

function saveAttachments_(timeQuery) {
  var folder = getFolder_();
  var query = 'has:attachment ' + timeQuery;
  var threads = GmailApp.search(query, 0, 100);
  threads.forEach(function (thread) {
    thread.getMessages().forEach(function (msg) {
      msg.getAttachments({ includeInlineImages: false, includeAttachments: true }).forEach(function (att) {
        var name = att.getName() || 'attachment';
        var ext = (name.split('.').pop() || '').toLowerCase();
        if (DOC_TYPES.indexOf(ext) === -1 || att.getSize() < 5000) return;
        var stamp = Utilities.formatDate(msg.getDate(), 'America/New_York', 'yyyy-MM-dd');
        var from = (msg.getFrom().match(/<(.+)>/) || [null, msg.getFrom()])[1];
        var fileName = stamp + ' | ' + from + ' | ' + name;
        if (folder.getFilesByName(fileName).hasNext()) return;
        var file = folder.createFile(att.copyBlob().setName(fileName));
        file.setDescription('Subject: ' + msg.getSubject() + '\nThread: ' + thread.getPermalink());
      });
    });
  });
}

function getFolder_() {
  var it = DriveApp.getFoldersByName(FOLDER_NAME);
  return it.hasNext() ? it.next() : DriveApp.createFolder(FOLDER_NAME);
}
