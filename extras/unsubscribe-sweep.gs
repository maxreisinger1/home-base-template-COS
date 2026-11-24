/**
 * Unsubscribe sweep v2 for your work Gmail. NOT yet tested in Apps Script.
 *
 * How it fits with Inbox Quest (World 3: Unsub Run):
 *   - In Quest you press UNSUBSCRIBE on a sender. Quest puts the Gmail label "Unsub/approved" on that sender's recent mail.
 *   - This script finds mail with that label, reads each sender's unsubscribe header, and unsubscribes.
 *   - Success: the mail is relabeled "Unsub/done". Anything it can't do automatically: "Unsub/needs-click".
 *     Quest's "Check script progress" lists those with a link to open each email, so you click unsubscribe yourself.
 *
 * It only ever acts on mail YOU approved in Quest. It never deletes or archives anything, and it skips
 * the NEVER_TOUCH senders even if one is labeled by mistake.
 *
 * SET UP (once)
 *   1. script.google.com, signed in as your work account. New project, paste this file.
 *   2. Run previewApproved. Approve the permissions. Open the execution log: it lists what it WOULD do. Nothing changes.
 *   3. Run processApproved once for real, then installHourlyTrigger so it runs by itself every hour.
 */

var ALLOW_MAILTO = false;     // true = for senders that only offer an unsubscribe email address, send that request from your account.
var ALLOW_PLAIN_LINK = false; // true = also open non-one-click links with a plain request (often needs a confirm click, so may not stick).

var LABEL_APPROVED = 'Unsub/approved';
var LABEL_DONE = 'Unsub/done';
var LABEL_CLICK = 'Unsub/needs-click';

var NEVER_TOUCH = [
  'mercury.com', 'gusto.com', 'frame.io', 'americanexpress.com', 'shopify.com', 'atlassian.com',
  'carta.com', 'xero.com', 'clio.com', 'squarespace.com', 'slack-mail.com', 'asana.com',
  'stripe.com', 'paypal.com', 'yourcompany.com', 'read.ai', 'otter.ai'
];

function previewApproved() { run_(true); }
function processApproved() { run_(false); }

function installHourlyTrigger() {
  ScriptApp.getProjectTriggers().forEach(function (t) {
    if (t.getHandlerFunction() === 'processApproved') ScriptApp.deleteTrigger(t);
  });
  ScriptApp.newTrigger('processApproved').timeBased().everyHours(1).create();
  Logger.log('Hourly trigger installed.');
}

function label_(name) { return GmailApp.getUserLabelByName(name) || GmailApp.createLabel(name); }

function run_(dry) {
  Logger.log(dry ? 'PREVIEW (nothing changes)' : 'LIVE');
  var approved = GmailApp.getUserLabelByName(LABEL_APPROVED);
  if (!approved) { Logger.log('No "' + LABEL_APPROVED + '" label yet. Approve a sender in Quest first.'); return; }
  var done = label_(LABEL_DONE), click = label_(LABEL_CLICK);
  var threads = approved.getThreads(0, 50);
  Logger.log(threads.length + ' approved threads.');
  var outcome = {}; // sender address -> 'done' | 'click'

  threads.forEach(function (th) {
    var msgs = th.getMessages();
    var msg = msgs[msgs.length - 1];
    var from = msg.getFrom();
    var addr = ((from.match(/<([^>]+)>/) || [])[1] || from).toLowerCase();

    var result = outcome[addr];
    if (!result) { result = tryUnsubscribe_(msg, addr, from, dry); outcome[addr] = result; }

    if (!dry) {
      th.removeLabel(approved);
      th.addLabel(result === 'done' ? done : click);
    }
  });
  Logger.log('Finished. Re-check in Quest: World 3, Check script progress.');
}

function tryUnsubscribe_(msg, addr, from, dry) {
  if (NEVER_TOUCH.some(function (p) { return addr.indexOf(p) !== -1; })) {
    Logger.log('PROTECTED, left for you: ' + from); return 'click';
  }
  var raw = msg.getRawContent();
  var head = raw.split(/\r?\n\r?\n/)[0].replace(/\r?\n[ \t]+/g, ' ');
  var lu = (head.match(/^List-Unsubscribe:\s*(.+)$/im) || [])[1] || '';
  var oneClick = /^List-Unsubscribe-Post:.*One-Click/im.test(head);
  var https = (lu.match(/<(https?:[^>]+)>/i) || [])[1];
  var mailto = (lu.match(/<(mailto:[^>]+)>/i) || [])[1];

  if (https && oneClick) {
    Logger.log((dry ? 'WOULD one-click: ' : 'one-click: ') + from);
    if (dry) return 'done';
    try {
      var r = UrlFetchApp.fetch(https, { method: 'post', payload: 'List-Unsubscribe=One-Click', contentType: 'application/x-www-form-urlencoded', muteHttpExceptions: true, followRedirects: true });
      var c = r.getResponseCode(); Logger.log('   result ' + c);
      return (c >= 200 && c < 400) ? 'done' : 'click';
    } catch (e) { Logger.log('   failed: ' + e); return 'click'; }
  }
  if (mailto && ALLOW_MAILTO) {
    var m = mailto.replace(/^mailto:/i, '').split('?');
    var subj = (/subject=([^&]+)/i.exec(m[1] || '') || [])[1];
    Logger.log((dry ? 'WOULD email unsubscribe: ' : 'email unsubscribe: ') + from + ' -> ' + m[0]);
    if (dry) return 'done';
    try { GmailApp.sendEmail(m[0], subj ? decodeURIComponent(subj) : 'unsubscribe', 'unsubscribe'); return 'done'; }
    catch (e) { Logger.log('   failed: ' + e); return 'click'; }
  }
  if (https && ALLOW_PLAIN_LINK) {
    Logger.log((dry ? 'WOULD open link: ' : 'open link: ') + from);
    if (dry) return 'done';
    try { var r2 = UrlFetchApp.fetch(https, { muteHttpExceptions: true }); return (r2.getResponseCode() < 400) ? 'done' : 'click'; }
    catch (e) { Logger.log('   failed: ' + e); return 'click'; }
  }
  Logger.log('MANUAL (needs your click): ' + from + (lu ? '' : ' [no unsubscribe header]'));
  return 'click';
}
