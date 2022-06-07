
"use strict";

let BoundingBoxes = require('./BoundingBoxes.js');
let ObjectCount = require('./ObjectCount.js');
let BoundingBox = require('./BoundingBox.js');
let CheckForObjectsGoal = require('./CheckForObjectsGoal.js');
let CheckForObjectsActionGoal = require('./CheckForObjectsActionGoal.js');
let CheckForObjectsActionFeedback = require('./CheckForObjectsActionFeedback.js');
let CheckForObjectsFeedback = require('./CheckForObjectsFeedback.js');
let CheckForObjectsAction = require('./CheckForObjectsAction.js');
let CheckForObjectsResult = require('./CheckForObjectsResult.js');
let CheckForObjectsActionResult = require('./CheckForObjectsActionResult.js');

module.exports = {
  BoundingBoxes: BoundingBoxes,
  ObjectCount: ObjectCount,
  BoundingBox: BoundingBox,
  CheckForObjectsGoal: CheckForObjectsGoal,
  CheckForObjectsActionGoal: CheckForObjectsActionGoal,
  CheckForObjectsActionFeedback: CheckForObjectsActionFeedback,
  CheckForObjectsFeedback: CheckForObjectsFeedback,
  CheckForObjectsAction: CheckForObjectsAction,
  CheckForObjectsResult: CheckForObjectsResult,
  CheckForObjectsActionResult: CheckForObjectsActionResult,
};
