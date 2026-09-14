# Connecto API Documentation

Total endpoints: 219

Interface: `com.neosoft.connecto.network.ApiService`

Base URLs (selected per-request by which Retrofit client instance is used):

| Client | Production base URL | Dev/staging base URL |
|---|---|---|
| Main app | `https://connecto.neosofttech.com/public/` | `https://connecto.php-dev.in/connecto/public/` |
| Knowledge base | `http://services.neosofttech.in/connect-to/` | - |
| CRM/Campaign | `https://crm.neosofttech.com/api/manage/` | `http://betacrm.neosofttech.com:3020/api/manage/` |
| Collab/SSO | `https://sso.neosofttech.com/sso-todos/` | (empty) |
| Support Tickets | `https://tickets.neosofttech.com/api/` | `https://neoticketportal.php-dev.in/api/` |
| RAB | `https://employee.neosofttech.com/` | `https://assessment.neosofttech.com/employee/` |

---

## POST ` api/v1/add-banner-views` [FormUrlEncoded]

- Method: `getBannerViewCount`
- Response: `DeleteMessageResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("banner_id") | `int` | `bannerId` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST ` api/v1/add-post-views` [FormUrlEncoded]

- Method: `getPostViewCount`
- Response: `DeleteMessageResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("post_id") | `int` | `postId` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST ` api/v1/delete-attendance-comment` [FormUrlEncoded]

- Method: `getCommentDelete`
- Response: `DeleteMessageResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("comment_id") | `int` | `comment_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST ` api/v1/update-attendance-comment` [FormUrlEncoded]

- Method: `getCommentUpdate`
- Response: `UpdateCommentResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("comment_id") | `int` | `comment_id` |
| Field("comment") | `String` | `comment` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `add-todo-update`

- Method: `addToDoUpdate`
- Response: `UpdateCollabResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Body | `JsonObject` | `json` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## GET `api/AssetTypes`

- Method: `demo`
- Response: `DemoResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Query("API_Key") | `String` | `userId` |

## POST `api/v1/add-attendance-comment` [FormUrlEncoded]

- Method: `getSubmitAttendanceComment`
- Response: `CommentSubmitResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("attendance_date") | `String` | `attendance_date` |
| Field("comment") | `String` | `comment` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/add-contact` [FormUrlEncoded]

- Method: `getAddContactAsync`
- Response: `AddDeleteContactResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `search_string` |
| Field("collegue_id") | `int` | `collegue_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/add-portfolio-suggestion` [FormUrlEncoded]

- Method: `getPortfolioResponseAsync`
- Response: `PortfolioResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Field("project_name") | `String` | `project_name` |
| Field("project_short_desc") | `String` | `project_short_desc` |
| Field("technical_desc") | `String` | `technical_desc` |
| Field("client_name") | `String` | `client_name` |
| Field("link") | `String` | `link` |
| Field("image") | `String` | `image` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/add-suggestion` [FormUrlEncoded]

- Method: `getAddSuggestionResponseAsync`
- Response: `AddSuggestionResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Field("type") | `String` | `type` |
| Field("subject") | `String` | `subject` |
| Field("description") | `String` | `description` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/add-three-sixty-degree-feedback` [FormUrlEncoded]

- Method: `getFeedbackSubmit`
- Response: `FeedbackSubmitResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `user_id` |
| Field("department_id") | `int` | `department_id` |
| Field("technology_id") | `int` | `technology_id` |
| Field("feedback_type") | `String` | `feedback_type` |
| Field("subject") | `String` | `subject` |
| Field("comments") | `String` | `comments` |
| Field("remarks") | `String` | `remarks` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/answer-poll` [FormUrlEncoded]

- Method: `getAnswerResponse`
- Response: `AnswerPollResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Field("poll_id") | `int` | `pollId` |
| Field("option_id") | `int` | `optionId` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/app_version_update` [FormUrlEncoded]

- Method: `getUpdateResponse`
- Response: `UpdateResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("version") | `int` | `version` |
| Field("os_type") | `String` | `os_type` |

## POST `api/v1/attendance-queries` [FormUrlEncoded]

- Method: `getAttendanceQuriesResponseAsync`
- Response: `AttendanceSummeryResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("attendance_date") | `String` | `attendance_date` |
| Field(NotificationCompat.CATEGORY_STATUS) | `int` | `status` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## GET `api/v1/attendance-queries-summary`

- Method: `getAttendanceQuerySummeryDetail`
- Response: `AttendanceQuerySummeryResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## GET `api/v1/attendance-queries/{id}`

- Method: `getAttendanceQueryDetail`
- Response: `AttendanceQueryDetail`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Path(encoded = false, value = "id") | `int` | `id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/attendee-checkin` [FormUrlEncoded]

- Method: `getMeetingCheckIn`
- Response: `CheckInResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("meeting_id") | `int` | `meeting_id` |
| Field("checkin_time") | `long` | `checkin_time` |
| Field("checkin_lat") | `double` | `checkin_lat` |
| Field("checkin_long") | `double` | `checkin_long` |
| Field("checkin_address") | `String` | `checkin_address` |
| Field("checkin_auto_lat") | `double` | `checkin_auto_lat` |
| Field("checkin_auto_long") | `double` | `checkin_auto_long` |
| Field("checkin_auto_address") | `String` | `checkin_auto_address` |
| Field("is_manual_checkin") | `boolean` | `is_manual_checkin` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/attendee-checkout` [FormUrlEncoded]

- Method: `getMeetingCheckOut`
- Response: `CheckOutResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("meeting_id") | `int` | `meeting_id` |
| Field("checkout_time") | `long` | `checkout_time` |
| Field("checkout_lat") | `double` | `checkout_lat` |
| Field("checkout_long") | `double` | `checkout_long` |
| Field("checkout_address") | `String` | `checkout_address` |
| Field("checkout_auto_lat") | `double` | `checkout_auto_lat` |
| Field("checkout_auto_long") | `double` | `checkout_auto_long` |
| Field("checkout_auto_address") | `String` | `checkout_auto_address` |
| Field("is_manual_checkout") | `boolean` | `is_manual_checkout` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/completed-chapter-reading` [FormUrlEncoded]

- Method: `getLLCompletedChaptersResponse`
- Response: `LLNextPageResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("topic_id") | `int` | `topic_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/delete-llab-goal` [FormUrlEncoded]

- Method: `getDeleteGoalResponse`
- Response: `LLNextPageResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("goal_id") | `int` | `goal_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/delete-question` [FormUrlEncoded]

- Method: `deleteQuestion`
- Response: `AwardedStatusViewedResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("question_id") | `int` | `questionId` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/delete-telegram-message` [FormUrlEncoded]

- Method: `getTelegramDeleteMsg`
- Response: `DeleteMessageResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field(Constants.MessagePayloadKeys.MSGID_SERVER) | `int` | `message_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/dynamic_connecto_details`

- Method: `getToolbarResponse`
- Response: `ToolbarResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## GET `api/v1/email-domains-listing`

- Method: `getDomain`
- Response: `DomainResponse`
- Parameters: none

## POST `api/v1/generate-attendance-query-request` [FormUrlEncoded]

- Method: `getMonthAttendanceQueryAsync`
- Response: `AttendanceQueryRequest`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Field("attendance_date") | `String` | `attendance_date` |
| Field("description") | `String` | `description` |
| Field("request_for") | `int` | `request_for` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-all-albums` [FormUrlEncoded]

- Method: `getAlbumResponseAsync`
- Response: `AlbumResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Field("year") | `String` | `year` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-all-contacts` [FormUrlEncoded]

- Method: `getSearchContactAsync`
- Response: `ContactResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("search_string") | `String` | `search_string` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-all-holiday` [FormUrlEncoded]

- Method: `holidaysListAsync`
- Response: `HolidayResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("year") | `int` | `year` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-all-mom` [FormUrlEncoded]

- Method: `getMomListing`
- Response: `MomListingResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("meeting_id") | `int` | `meeting_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-all-survey` [FormUrlEncoded]

- Method: `getAllSurveyAsync`
- Response: `SurveyResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-all-tagged-posts`

- Method: `getTaggedPostList`
- Response: `TaggedPostResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## GET `api/v1/get-all-todays-meeting-details`

- Method: `getTodaysMeetingResponse`
- Response: `TodayMeetingResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-all-user-media` [FormUrlEncoded]

- Method: `getPhotoListingResponse`
- Response: `PhotoListResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Field("album_id") | `int` | `album_id` |
| Field("offset") | `int` | `offset` |
| Field("year") | `String` | `year` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-asked-question`

- Method: `getAskedListResponse`
- Response: `AskedQuestionModelResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Body | `JsonObject` | `json` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-awarded-question`

- Method: `getAwardedListResponse`
- Response: `AwardedModelResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Body | `JsonObject` | `json` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-banners`

- Method: `getBannerList`
- Response: `BannerResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-checkList` [FormUrlEncoded]

- Method: `getDailyCheckListResponse`
- Response: `DailyChecklistResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-configuration-details` [FormUrlEncoded]

- Method: `getSettingResponse`
- Response: `SettingResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-departments`

- Method: `getDepartment`
- Response: `DepartmentResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-dynamic-more-tab`

- Method: `moreDynamic`
- Response: `NewMoreResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `token` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-expenses-list` [FormUrlEncoded]

- Method: `getExpenseListing`
- Response: `ExpenseListingResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("meeting_id") | `int` | `meeting_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-helped-question`

- Method: `getHelpedListResponse`
- Response: `AskedQuestionModelResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Body | `JsonObject` | `json` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-job-openings` [FormUrlEncoded]

- Method: `getRabNewListing`
- Response: `RabNewResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("search_keyword") | `String` | `search_keyword` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-last-call-at`

- Method: `getCallLogTime`
- Response: `CallLogTimeResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-latest-screen-data` [FormUrlEncoded]

- Method: `getLatestScreenResponse`
- Response: `com.neosoft.connecto.model.response.latest.allapis.LatestResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Field("offset") | `int` | `pageNumber` |
| Field("version") | `int` | `version` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Field("os_type") | `String` | `device_token` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## GET `api/v1/get-leaderboard`

- Method: `getLeaderboard`
- Response: `LeaderboardModelResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## GET `api/v1/get-leaderboard-helped`

- Method: `getHelpedLeaderboard`
- Response: `LeaderboardModelResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-learning-lab-progress`

- Method: `getLLProgressResponse`
- Response: `LLProgressResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-list` [FormUrlEncoded]

- Method: `getMessageListing`
- Response: `MessageListingResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("id") | `int` | `id` |
| Field("user_id") | `int` | `user_id` |
| Field("type") | `String` | `type` |
| Field("offset") | `int` | `offset` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-meeting-cards` [FormUrlEncoded]

- Method: `getCardResposne`
- Response: `CardsResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("check_id") | `int` | `check_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-meeting-details` [FormUrlEncoded]

- Method: `getMeetingDetails`
- Response: `MeetingDetailsResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("meeting_id") | `int` | `meeting_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-meetings-by-month` [FormUrlEncoded]

- Method: `getPreviousMeetingMonthlyResposne`
- Response: `PreviousMeetingMonthlyResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `user_id` |
| Field("month") | `String` | `month` |
| Field("page") | `int` | `page` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-month-attendance` [FormUrlEncoded]

- Method: `getMonthAttendanceAsync`
- Response: `AttendanceMonthResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Field("attendance_month") | `int` | `attendance_month` |
| Field("attendance_year") | `int` | `attendance_year` |
| Field("send_checklist_data") | `int` | `send_checklist_data` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-month-attendance-summery` [FormUrlEncoded]

- Method: `getMonthAttendanceSummeryAsync`
- Response: `AttendanceMonthSummeryResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Field("attendance_month") | `int` | `attendance_month` |
| Field("attendance_year") | `int` | `attendance_year` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-mpin-otp`

- Method: `getMPin`
- Response: `MPinResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header("generate_otp") | `boolean` | `generate_otp` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-my-contacts` [FormUrlEncoded]

- Method: `getMyContactAsync`
- Response: `ContactResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `search_string` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-my-wall-post-list` [FormUrlEncoded]

- Method: `getMyWallPostList`
- Response: `PostResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Field("wop_option_id") | `int` | `optionId` |
| Field("month") | `Integer` | `month` |
| Field("technology_id") | `Integer` | `technologyId` |
| Field("offset") | `Integer` | `offset` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-portfolio-details` [FormUrlEncoded]

- Method: `getPortfolioDetail`
- Response: `PortfolioDetailResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("id") | `int` | `id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-post-like-user-list` [FormUrlEncoded]

- Method: `getWopLikeMember`
- Response: `LikeMemberResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("wop_wall_id") | `int` | `wop_wall_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-project-user-list` [FormUrlEncoded]

- Method: `getProjectUserList`
- Response: `UserResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("wop_wall_id") | `int` | `postId` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-question` [FormUrlEncoded]

- Method: `getimproveQuestion`
- Response: `ImproveQuestionResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("question_id") | `int` | `question_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-question-details` [FormUrlEncoded]

- Method: `getdetailedListResponse`
- Response: `DetailListResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("question_id") | `int` | `question_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-rab-leaderboard`

- Method: `getRabReward`
- Response: `RabRewardResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-rnr`

- Method: `getRnr`
- Response: `Rnr`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-run-time-update-data` [FormUrlEncoded]

- Method: `getRunTimeResponse`
- Response: `RuntimeResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Field("version") | `int` | `version` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Field("os_type") | `String` | `device_token` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-submitted-checklists` [FormUrlEncoded]

- Method: `getSubmittedCheckList`
- Response: `SubmittedChecklistResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `token` |
| Field("attendance_date") | `String` | `date` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-subtechnology` [FormUrlEncoded]

- Method: `getSubTechnologyList`
- Response: `TechnologyResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("technology_id") | `int` | `technology_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-survey-questions` [FormUrlEncoded]

- Method: `getAllQuestionSurvey`
- Response: `SurveyQuestionResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("survey_id") | `int` | `userId` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-technologies` [FormUrlEncoded]

- Method: `getTechnology`
- Response: `TechnologyResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("department_id") | `int` | `department_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## GET `api/v1/get-technology`

- Method: `getTechnologyList`
- Response: `TechnologyListResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-three-sixty-degree-feedback` [FormUrlEncoded]

- Method: `getFeedbackListing`
- Response: `FeedbackListingResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-tip-details` [FormUrlEncoded]

- Method: `getTipsDetailsAsync`
- Response: `TipDetailResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("topic_id") | `int` | `topic_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-todays-attendance` [FormUrlEncoded]

- Method: `getTodayAttendance`
- Response: `AttendanceMonthResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## GET `api/v1/get-update-request-dropdown-list`

- Method: `getUpdateProfileDropDown`
- Response: `UpdateProfileDropDownResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## GET `api/v1/get-user-awards-count`

- Method: `getAwardCount`
- Response: `QuestionFeedbackModelResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-user-list` [FormUrlEncoded]

- Method: `getUserList`
- Response: `UserResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Field("keyword") | `String` | `optionId` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-user-selected-sub-categories`

- Method: `getSelectedTechnologies`
- Response: `SelectedTechnologiesResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-vcard-detail` [FormUrlEncoded]

- Method: `getNewProfile`
- Response: `ProfileNewResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `user_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-wall-post-list` [FormUrlEncoded]

- Method: `getWallPostList`
- Response: `PostResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Field("wop_option_id") | `int` | `optionId` |
| Field("month") | `Integer` | `month` |
| Field("technology_id") | `Integer` | `technologyId` |
| Field("offset") | `Integer` | `offset` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-wop-option-list` [FormUrlEncoded]

- Method: `getWopOptionList`
- Response: `OptionsResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("month") | `Integer` | `monthNo` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/get-wop-option-templates` [FormUrlEncoded]

- Method: `getOptionTemplates`
- Response: `TemplateResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Field("wop_option_id") | `int` | `optionId` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/important-contact`

- Method: `getImportantContactResponse`
- Response: `ImportantContactResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/job-details` [FormUrlEncoded]

- Method: `getRabNewDetail`
- Response: `RabDetailResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("job_id") | `String` | `job_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/learning-lab-ask-question` [FormUrlEncoded]

- Method: `getAskQuestionResponse`
- Response: `LLNextPageResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("tip_id") | `int` | `tip_id` |
| Field("topic_id") | `int` | `tag_id` |
| Field("question") | `String` | `question` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/learning-lab-bookmark-card` [FormUrlEncoded]

- Method: `getSetNewTagResponse`
- Response: `LLNextPageResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("card_id") | `int` | `card_id` |
| Field("save_tag") | `int` | `save_tag` |
| Field("user_on_page_num") | `int` | `user_on_page_num` |
| Field("topic_id") | `int` | `topic_id` |
| Field(AppMeasurementSdk.ConditionalUserProperty.NAME) | `String` | `name` |
| Field("color_code") | `String` | `color_code` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/learning-lab-bookmark-card` [FormUrlEncoded]

- Method: `getSetTagResponse`
- Response: `LLNextPageResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("tag_id") | `int` | `tag_id` |
| Field("card_id") | `int` | `card_id` |
| Field("save_tag") | `int` | `save_tag` |
| Field("user_on_page_num") | `int` | `user_on_page_num` |
| Field("topic_id") | `int` | `topic_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/learning-lab-get-bookmark-cards-by-tag` [FormUrlEncoded]

- Method: `getBookmarkListResponse`
- Response: `BookmarkListingResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("tag_id") | `int` | `tag_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## GET `api/v1/learning-lab-get-tags`

- Method: `getTagListingResponse`
- Response: `TagListingResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/learning-lab-remove-tag` [FormUrlEncoded]

- Method: `getDeleteTagResponse`
- Response: `LLNextPageResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("tag_id") | `int` | `tag_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/learning-lab-save-issue` [FormUrlEncoded]

- Method: `getRAIResponse`
- Response: `LLNextPageResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("tip_id") | `int` | `tip_id` |
| Field("topic_id") | `int` | `tag_id` |
| Field("issue") | `String` | `issue` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/learning-lab-save-tags` [FormUrlEncoded]

- Method: `getSaveTagsResponse`
- Response: `LLNextPageResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field(AppMeasurementSdk.ConditionalUserProperty.NAME) | `String` | `name` |
| Field("color_code") | `String` | `color_code` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/learning-labs-category-details` [FormUrlEncoded]

- Method: `getCategoryResponse`
- Response: `LLCategoryResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("category_id") | `int` | `category_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/learning-labs-category-list`

- Method: `getLLResponse`
- Response: `LLResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/learning-labs-chapter-details` [FormUrlEncoded]

- Method: `getLLDetailsResponse`
- Response: `LLDetailsResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("topic_id") | `int` | `topic_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/learning-labs-set-goals` [FormUrlEncoded]

- Method: `getSetGoalResponse`
- Response: `GoalSetResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("cards_per_day") | `int` | `cards_per_day` |
| Field("is_reminder_set") | `int` | `is_reminder_set` |
| Field("reminder_time") | `String` | `reminder_time` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/like-unlike-post` [FormUrlEncoded]

- Method: `getLikeUnlike`
- Response: `LikeUnlikeResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Field("post_id") | `int` | `pollId` |
| Field("media_id") | `int` | `media_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/like-unlike-topic` [FormUrlEncoded]

- Method: `getTopicsLikeUnlike`
- Response: `TopicsLikeDislikeResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Field("topic_id") | `int` | `topic_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/list-group-members` [FormUrlEncoded]

- Method: `getParticipantList`
- Response: `ParticipantListingResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field(FirebaseAnalytics.Param.GROUP_ID) | `int` | `group_id` |
| Field("group_type") | `String` | `group_type` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/list-meetings` [FormUrlEncoded]

- Method: `getListOfMeeting`
- Response: `MeetingListResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("year") | `String` | `year` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/list-messages-group` [FormUrlEncoded]

- Method: `listMessageGroup`
- Response: `MessageGroupModel`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/list-portfolio-suggestions` [FormUrlEncoded]

- Method: `getPortfolioListing`
- Response: `PortfolioListingResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/list-question`

- Method: `getQuestion`
- Response: `QuestionModelResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Body | `JsonObject` | `json` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/list-tip-topics` [FormUrlEncoded]

- Method: `getTipsListAsync`
- Response: `TipsListResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("category_id") | `int` | `category_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/llab-month-wise-updates`

- Method: `getMonthWiseResponse`
- Response: `MonthWiseResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/llab-month-wise-updates` [FormUrlEncoded]

- Method: `getMonthWiseResponseMonth`
- Response: `MonthWiseResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("month") | `String` | `month` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/logout` [FormUrlEncoded]

- Method: `logout`
- Response: `LogoutResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `Integer` | `id` |
| Field("udid") | `String` | `udid` |
| Field("device_token") | `String` | `device_token` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/meetings-checkin` [FormUrlEncoded]

- Method: `getMeetingCheckInResponse`
- Response: `MeetingCheckInResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Field("checkin_lat") | `String` | `checkInLat` |
| Field("checkin_long") | `String` | `checkInLong` |
| Field("checkin_address") | `String` | `checkInAddress` |
| Field("meeting_company") | `String` | `meetingCompany` |
| Field("meeting_location") | `String` | `meetingLocation` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/meetings-checkout` [FormUrlEncoded]

- Method: `getMeetingCheckOutResponse`
- Response: `MeetingCheckOutResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("check_id") | `int` | `check_id` |
| Field("checkout_lat") | `String` | `checkInLat` |
| Field("checkout_long") | `String` | `checkInLong` |
| Field("checkout_address") | `String` | `checkout_address` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/message-read-unread-count` [FormUrlEncoded]

- Method: `getTelegramCount`
- Response: `TelegramCountResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field(Constants.MessagePayloadKeys.MSGID_SERVER) | `int` | `message_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/my-photos` [FormUrlEncoded]

- Method: `getUserPhotosAsync`
- Response: `PhotoListResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Field("offset") | `int` | `offset` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/notification-detail` [FormUrlEncoded]

- Method: `getNotificationDetailAsync`
- Response: `NotificationDetailResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("notification_id") | `int` | `notification_id` |
| Field("is_read") | `int` | `is_read` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/notification-list` [FormUrlEncoded]

- Method: `getNotificationListResponseAsync`
- Response: `NotificationResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/polls` [FormUrlEncoded]

- Method: `getPollsResponse`
- Response: `PollsResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/posts` [FormUrlEncoded]

- Method: `getLatestResponse`
- Response: `LatestResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Field("offset") | `int` | `pageNumber` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/profile-update` [FormUrlEncoded]

- Method: `getUserUpdate`
- Response: `UserUpdateResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `id` |
| Field("profile_image") | `String` | `profile_image` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/read-new-tab` [FormUrlEncoded]

- Method: `readStatusChangeApi`
- Response: `ReadStatusResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `user_id` |
| Field("menu_id") | `int` | `menu_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `token` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/remove-contact` [FormUrlEncoded]

- Method: `getDeleteContactAsync`
- Response: `AddDeleteContactResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `search_string` |
| Field("collegue_id") | `int` | `collegue_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/resend-otp` [FormUrlEncoded]

- Method: `reSendOtpAsync`
- Response: `Object`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("email") | `String` | `str` |
|  | `Continuation<? super Response<LoginModel>>` | `continuation` |

## POST `api/v1/reset-learning-lab-progress`

- Method: `getLLProgressResetResponse`
- Response: `LLNextPageResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/save-answer`

- Method: `submitAnswer`
- Response: `SurveySubmitResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Body | `JsonObject` | `json` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/save-awarded-viewed-status` [FormUrlEncoded]

- Method: `saveAwardViewedStatus`
- Response: `AwardedStatusViewedResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("award_id") | `int` | `awardId` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/save-call-history`

- Method: `saveCallLog`
- Response: `CallLogSubmitResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Body | `JsonObject` | `json` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/save-categories-by-user`

- Method: `submitTechnologies`
- Response: `SubmitTechnologiesResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Body | `JsonObject` | `json` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/save-checkList-response`

- Method: `submitDailyChecklist`
- Response: `DailyChecklistSubmitResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Body | `JsonObject` | `json` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/save-expenses` [FormUrlEncoded]

- Method: `submitExpense`
- Response: `ExpenseSubmitResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("meeting_id") | `int` | `meeting_id` |
| Field("date") | `String` | `date` |
| Field("amount") | `String` | `amount` |
| Field("description") | `String` | `description` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/save-meetings-checkin-checkout-cards` [FormUrlEncoded]

- Method: `getCardUploadResponse`
- Response: `MeetingCheckInResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("check_id") | `int` | `check_id` |
| Field("card_image") | `String` | `card_image` |
| Field("card_comment") | `String` | `card_comment` |
| Field("card_identifier") | `String` | `card_identifier` |
| Field("card_type") | `String` | `card_type` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/save-post-like` [FormUrlEncoded]

- Method: `wallPostLikeUnlike`
- Response: `WallPostLikeUnlikeResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Field("wop_wall_id") | `int` | `optionId` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/save-question` [FormUrlEncoded]

- Method: `getAddQuestion`
- Response: `AddQuestionResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("title") | `String` | `type` |
| Field("user_id") | `int` | `user_id` |
| Field("category_id") | `int` | `category_id` |
| Field("sub_cat_id") | `int` | `sub_cat_id` |
| Field(Constants.FirelogAnalytics.PARAM_PRIORITY) | `String` | `priority` |
| Field("detail") | `String` | `detail` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/save-user-topic-current-page-no` [FormUrlEncoded]

- Method: `getLLPageResponse`
- Response: `LLNextPageResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("topic_id") | `int` | `topic_id` |
| Field("tip_id") | `int` | `tip_id` |
| Field("user_on_page_num") | `int` | `user_on_page_num` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/save-wall-post`

- Method: `saveWallPost`
- Response: `SaveWallResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Body | `JsonObject` | `json` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/save_configuration_setting`

- Method: `submitSetting`
- Response: `SettingResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Body | `JsonObject` | `json` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/scoreboard/dashboard` [FormUrlEncoded]

- Method: `getScoreboardData`
- Response: `ScoreboardResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("selectedDay") | `String` | `selectedDay` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `accept` |

## POST `api/v1/search-attendee` [FormUrlEncoded]

- Method: `getAttendeeSearch`
- Response: `SearchMeetingResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("search_string") | `String` | `search_string` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/search-company` [FormUrlEncoded]

- Method: `getCompanyResponse`
- Response: `CompanyResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("search_string") | `String` | `search_string` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/search-company-contact` [FormUrlEncoded]

- Method: `getCompanyContact`
- Response: `CompanyContactResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("search_string") | `String` | `search_string` |
| Field("company_id") | `int` | `company_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/set-award` [FormUrlEncoded]

- Method: `getGiveAwardResponse`
- Response: `GiveAwardModelResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("question_id") | `int` | `question_id` |
| Field("reward_for_user") | `int` | `user_id` |
| Field("type") | `String` | `type` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/set-help` [FormUrlEncoded]

- Method: `gethelpResponse`
- Response: `HelpModelResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("question_id") | `int` | `question_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/set-improve-question-request` [FormUrlEncoded]

- Method: `getimproveResponse`
- Response: `ImproveQuestionModelResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("question_id") | `int` | `question_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/show-contact`

- Method: `getContactShowResponse`
- Response: `ContactShowResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/sign-in` [FormUrlEncoded]

- Method: `getAttendanceSignInAsync`
- Response: `PunchInResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Field("attendance_date") | `String` | `attendance_date` |
| Field("signin_image") | `String` | `signin_image` |
| Field("manual_latitude") | `String` | `latitude` |
| Field("manual_longitude") | `String` | `longitude` |
| Field("signin_address") | `String` | `signout_address` |
| Field("is_manual_signin") | `String` | `is_manual_signout` |
| Field("auto_latitude") | `String` | `auto_latitude` |
| Field("auto_longitude") | `String` | `auto_longitude` |
| Field("config_id") | `int` | `config_id` |
| Field("reason") | `String` | `reason` |
| Field("reason_title") | `String` | `reason_title` |
| Field("employee_mood") | `int` | `employee_mood` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/sign-out` [FormUrlEncoded]

- Method: `getAttendanceSignOutAsync`
- Response: `PunchOutResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Field("attendance_date") | `String` | `attendance_date` |
| Field("signout_image") | `String` | `signin_image` |
| Field("manual_latitude") | `String` | `latitude` |
| Field("manual_longitude") | `String` | `longitude` |
| Field("signout_address") | `String` | `signout_address` |
| Field("is_manual_signout") | `String` | `is_manual_signout` |
| Field("auto_latitude") | `String` | `auto_latitude` |
| Field("auto_longitude") | `String` | `auto_longitude` |
| Field("config_id") | `int` | `config_id` |
| Field("reason") | `String` | `reason` |
| Field("reason_title") | `String` | `reason_title` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/sso-verification`

- Method: `getChatBotURL`
- Response: `ChatBotResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/store-meeting` [FormUrlEncoded]

- Method: `submitAddMeetingData`
- Response: `AddMeetingSubmitResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("meeting_type") | `String` | `meeting_type` |
| Field("meeting_title") | `String` | `meeting_title` |
| Field("meeting_agenda") | `String` | `meeting_agenda` |
| Field("meeting_address") | `String` | `meeting_address` |
| Field("meeting_city") | `String` | `meeting_city` |
| Field("meeting_lat") | `String` | `meeting_lat` |
| Field("meeting_long") | `String` | `meeting_long` |
| Field("meeting_schedule") | `long` | `meeting_schedule` |
| Field("meeting_reminder") | `long` | `meeting_reminder` |
|  | `@FieldMap Map<String, String>` | `attendeesList` |
| Field("company_id") | `int` | `company_id` |
| Field("company_name") | `String` | `company_name` |
| Field("client_id") | `int` | `client_id` |
| Field("client_name") | `String` | `client_name` |
| Field("client_email") | `String` | `client_email` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/store-message` [FormUrlEncoded]

- Method: `getMessageSending`
- Response: `MessageSendResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("id") | `int` | `id` |
| Field("user_id") | `int` | `user_id` |
| Field("text") | `String` | `text` |
| Field("type") | `String` | `type` |
| Field("image") | `String` | `image` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/store-mom` [FormUrlEncoded]

- Method: `addMom`
- Response: `AddMomResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("meeting_id") | `int` | `meeting_id` |
| Field("added_date") | `String` | `added_date` |
| Field("description") | `String` | `description` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/suggestion-list` [FormUrlEncoded]

- Method: `getSuggestionListAsync`
- Response: `SuggestionResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/suggestion-type-list`

- Method: `getSuggestionTypeListAsync`
- Response: `SuggestionTypeResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/tip-category-list`

- Method: `getTipsCategoriesResponse`
- Response: `TipsCategoriesResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/unbookmark-card` [FormUrlEncoded]

- Method: `getUnBookmarkResponse`
- Response: `LLNextPageResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("card_id") | `int` | `card_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/update-attendance-query` [FormUrlEncoded]

- Method: `getUpdateAttendanceQueryAsync`
- Response: `UpdateAttendanceQueryResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("attendance_query_id") | `int` | `attendance_query_id` |
| Field(NotificationCompat.CATEGORY_STATUS) | `int` | `status` |
| Field("update_attendance_remark") | `int` | `update_attendance_remark` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/update-portfolio-suggestion` [FormUrlEncoded]

- Method: `updatePortfolioDetail`
- Response: `UpdateDetailResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("id") | `int` | `id` |
| Field("user_id") | `int` | `userId` |
| Field("project_name") | `String` | `project_name` |
| Field("project_short_desc") | `String` | `project_short_desc` |
| Field("technical_desc") | `String` | `technical_desc` |
| Field("client_name") | `String` | `client_name` |
| Field("link") | `String` | `link` |
| Field("image") | `String` | `image` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/update-question` [FormUrlEncoded]

- Method: `updateQuestion`
- Response: `AddQuestionResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("question_id") | `int` | `question_id` |
| Field("title") | `String` | `type` |
| Field(Constants.FirelogAnalytics.PARAM_PRIORITY) | `String` | `priority` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/update-vcard-details` [FormUrlEncoded]

- Method: `getUpdateProfile`
- Response: `UpdateProfileResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Field("title") | `String` | `title` |
| Field("description") | `String` | `description` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/upload-media` [FormUrlEncoded]

- Method: `getUploadImageVideo`
- Response: `UploadMediaResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Field("media_data") | `String` | `media_data` |
| Field("media_type") | `String` | `media_type` |
| Field("album_id") | `int` | `album_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/user-profile` [FormUrlEncoded]

- Method: `getUserProfileAsync`
- Response: `UserProfileResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("user_id") | `int` | `userId` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `api/v1/validate-email` [FormUrlEncoded]

- Method: `loginAsync`
- Response: `Object`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("email") | `String` | `str` |
| Field("udid") | `String` | `str2` |
| Field("device_token") | `String` | `str3` |
| Field("device_os") | `String` | `str4` |
|  | `Continuation<? super Response<LoginModel>>` | `continuation` |

## POST `api/v1/validate-email-new-device-request` [FormUrlEncoded]

- Method: `changeDeviceEmail`
- Response: `ChangeDeviceEmailResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("email") | `String` | `email` |

## POST `api/v1/validate-otp` [FormUrlEncoded]

- Method: `otpValidateAsync`
- Response: `OtpResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("email") | `String` | `email` |
| Field("otp") | `String` | `otp` |

## POST `api/v1/validate-otp-new-device` [FormUrlEncoded]

- Method: `changeDeviceOTP`
- Response: `ChangeDeviceEmailResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("email") | `String` | `email` |
| Field("otp") | `String` | `otp` |
| Field("udid") | `String` | `udid` |
| Field("device_token") | `String` | `device_token` |
| Field("device_os") | `String` | `device_os` |

## GET `api/v1/year_listing`

- Method: `getYearResponse`
- Response: `YearResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `auth/connecto-login`

- Method: `getVisitorLogin`
- Response: `VisitorLoginResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Body | `JsonObject` | `json` |

## POST `authenticate` [FormUrlEncoded]

- Method: `getTicketLoginResponse`
- Response: `TicketLoginResponseNew`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Field("username") | `String` | `userId` |
| Field("password") | `String` | `optionId` |
| Field("device_token") | `String` | `device_token` |
| Field("device_type") | `String` | `device_type` |

## GET `campaign-type/get-list-api`

- Method: `getCampaignType`
- Response: `CampaignTypeResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## GET `campaign-type/get-list-with-campaign-api`

- Method: `getCampaignAsync`
- Response: `CampaignResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## GET `campaign/get-executive-api`

- Method: `getLeadExecutive`
- Response: `LeadExecutiveResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Query("campaign_id") | `int` | `campaign_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## GET `campaign/get-list-api`

- Method: `getEventCampaignType`
- Response: `EventCampaignResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Query("le1") | `String` | `client_type_id` |
| Query("le2") | `String` | `campaign_type_name` |
| Query("ok") | `String` | `abc` |
| Query("ov") | `String` | `asc` |

## GET `campaign/get-list-for-lead-api`

- Method: `getLeadCampaign`
- Response: `LeadCampaignResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Query("wv") | `int` | `wv` |
| Query("wk") | `String` | `wk` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## GET `campaign/get-list-for-lead-api`

- Method: `getLeadfilterCampaign`
- Response: `LeadCampaignResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Query("search_value") | `String` | `search_value` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## GET `categories-status-by-category-id/{categoryid}`

- Method: `getcollabStages`
- Response: `StagesCollabResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Path(encoded = false, value = "categoryid") | `int` | `categoryid` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## GET `city-master/get-list-api`

- Method: `getLeadLocation`
- Response: `LocationResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Query("le1") | `String` | `le1` |
| Query("le2") | `String` | `le2` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `client-company/api`

- Method: `addleadcompany`
- Response: `AddLeadCompanyAccountResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Body | `JsonObject` | `json` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## GET `client-company/get-list-by-company-name/api`

- Method: `getVisitorCompany`
- Response: `VisitorCompanyResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Query("q") | `String` | `q` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Query("le1") | `String` | `le1` |
| Query("le2") | `String` | `le2` |
| Query("wk") | `String` | `wk` |
| Query("wv") | `int` | `wv` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `client-master/add-lead-cards/api`

- Method: `addLeadCard`
- Response: `AddLeadCardResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Body | `JsonObject` | `json` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `client-master/client-list/api`

- Method: `getLeadList`
- Response: `LeadListingResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Body | `JsonObject` | `json` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `client-master/create-lead/api`

- Method: `submitLead`
- Response: `LeadSubmitResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Body | `JsonObject` | `json` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `client-master/delete-lead-card/api`

- Method: `deleteLeadCard`
- Response: `RemoveAttachCardResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Body | `JsonObject` | `json` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## GET `client-master/get-lead/api`

- Method: `getLeadDetails`
- Response: `LeadDetailsResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Query("client_id") | `Integer` | `client_id` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## GET `client-type/get-list-api`

- Method: `getClientType`
- Response: `ClientTypeReponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Query("le1") | `String` | `client_type_id` |
| Query("le2") | `String` | `client_type_title` |

## POST `collab-login`

- Method: `getCollabLogin`
- Response: `CollabLoginResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Body | `JsonObject` | `json` |

## GET `company-master/get-list/api`

- Method: `getLeadCompany`
- Response: `LeadCompanyResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Query("le1") | `String` | `le1` |
| Query("le2") | `String` | `le2` |
| Query("ok") | `String` | `ok` |
| Query("ov") | `String` | `ov` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `connecto-api/add-refer-buddy` [Multipart]

- Method: `addRab`
- Response: `AddRabResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Query("token") | `String` | `token` |
| Part("is_experience") | `RequestBody` | `is_experience` |
| Part("experience_id") | `RequestBody` | `experience_id` |
| Part("department_id") | `RequestBody` | `department_id` |
| Part("technology_id") | `RequestBody` | `technology_id` |
| Part("position_applied_for") | `RequestBody` | `position_applied_for` |
| Part("first_name") | `RequestBody` | `first_name` |
| Part("last_name") | `RequestBody` | `last_name` |
| Part("candidate_email") | `RequestBody` | `candidate_email` |
| Part("mobile_code") | `RequestBody` | `mobile_code` |
| Part("candidate_mobile") | `RequestBody` | `candidate_mobile` |
| Part("city_id") | `RequestBody` | `city_id` |
| Part("candidate_remark") | `RequestBody` | `candidate_remark` |

## POST `connecto-api/add-refer-buddy` [Multipart]

- Method: `addRab`
- Response: `AddRabResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Query("token") | `String` | `token` |
| Part("is_experience") | `RequestBody` | `is_experience` |
| Part("experience_id") | `RequestBody` | `experience_id` |
| Part("department_id") | `RequestBody` | `department_id` |
| Part("technology_id") | `RequestBody` | `technology_id` |
| Part("position_applied_for") | `RequestBody` | `position_applied_for` |
| Part("first_name") | `RequestBody` | `first_name` |
| Part("last_name") | `RequestBody` | `last_name` |
| Part("candidate_email") | `RequestBody` | `candidate_email` |
| Part("mobile_code") | `RequestBody` | `mobile_code` |
| Part("candidate_mobile") | `RequestBody` | `candidate_mobile` |
| Part("city_id") | `RequestBody` | `city_id` |
| Part("candidate_remark") | `RequestBody` | `candidate_remark` |
| Part | `MultipartBody.Part` | `candidate_resume` |

## GET `connecto-api/country-code`

- Method: `getCountryCode`
- Response: `RabCountryCodeResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Query("token") | `String` | `token` |

## POST `connecto-api/delete-refer`

- Method: `getRabRemove`
- Response: `RabRemoveResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Query("token") | `String` | `token` |
| Body | `JsonObject` | `json` |

## GET `connecto-api/departments`

- Method: `getrabDepartment`
- Response: `RabDepartmenttResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Query("token") | `String` | `token` |

## POST `connecto-api/experience-level`

- Method: `getrabExperience`
- Response: `RabExperienceResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Query("token") | `String` | `token` |
| Body | `JsonObject` | `json` |

## POST `connecto-api/get-by-id`

- Method: `getRabDetail`
- Response: `RabGetDetailResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Query("token") | `String` | `token` |
| Body | `JsonObject` | `json` |

## POST `connecto-api/get-tech-role`

- Method: `getrabTechnologyRoles`
- Response: `TechnologyRolesResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Query("token") | `String` | `token` |
| Body | `JsonObject` | `json` |

## POST `connecto-api/list-buddy`

- Method: `getRabListing`
- Response: `RabListingResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Query("token") | `String` | `token` |
| Body | `JsonObject` | `json` |

## GET `connecto-api/location`

- Method: `getLocationRab`
- Response: `RabLocationResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Query("token") | `String` | `token` |

## POST `connecto-api/login`

- Method: `getRabLogin`
- Response: `RabLoginResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Body | `JsonObject` | `json` |

## POST `connecto-api/update-buddy` [Multipart]

- Method: `getRabUpdate`
- Response: `RabUpdateResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Query("token") | `String` | `token` |
| Part("is_experience") | `RequestBody` | `is_experience` |
| Part("experience_id") | `RequestBody` | `experience_id` |
| Part("department_id") | `RequestBody` | `department_id` |
| Part("technology_id") | `RequestBody` | `technology_id` |
| Part("position_applied_for") | `RequestBody` | `position_applied_for` |
| Part("first_name") | `RequestBody` | `first_name` |
| Part("last_name") | `RequestBody` | `last_name` |
| Part("candidate_email") | `RequestBody` | `candidate_email` |
| Part("mobile_code") | `RequestBody` | `mobile_code` |
| Part("candidate_mobile") | `RequestBody` | `candidate_mobile` |
| Part("city_id") | `RequestBody` | `city_id` |
| Part("candidate_remark") | `RequestBody` | `candidate_remark` |
| Part("ref_id") | `RequestBody` | `refid` |

## POST `connecto-api/update-buddy` [Multipart]

- Method: `getRabUpdate`
- Response: `RabUpdateResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Query("token") | `String` | `token` |
| Part("is_experience") | `RequestBody` | `is_experience` |
| Part("experience_id") | `RequestBody` | `experience_id` |
| Part("department_id") | `RequestBody` | `department_id` |
| Part("technology_id") | `RequestBody` | `technology_id` |
| Part("position_applied_for") | `RequestBody` | `position_applied_for` |
| Part("first_name") | `RequestBody` | `first_name` |
| Part("last_name") | `RequestBody` | `last_name` |
| Part("candidate_email") | `RequestBody` | `candidate_email` |
| Part("mobile_code") | `RequestBody` | `mobile_code` |
| Part("candidate_mobile") | `RequestBody` | `candidate_mobile` |
| Part("city_id") | `RequestBody` | `city_id` |
| Part("candidate_remark") | `RequestBody` | `candidate_remark` |
| Part("ref_id") | `RequestBody` | `refid` |
| Part | `MultipartBody.Part` | `candidate_resume` |

## GET `country-master/get-list`

- Method: `getCountryResponseAsync`
- Response: `CountryResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `create-todo`

- Method: `createToDo`
- Response: `CreateCollabResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Body | `JsonObject` | `json` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## GET `designation/get-list/api`

- Method: `getLeadDesignation`
- Response: `DesignationResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Query("le1") | `String` | `le1` |
| Query("le2") | `String` | `le2` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `event-lead`

- Method: `submitEvent`
- Response: `ClientTypeReponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Body | `JsonObject` | `json` |

## POST `event-lead/api`

- Method: `submitEvent`
- Response: `EventSubmitResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Body | `JsonObject` | `json` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## GET `get-todo-by-id/{todoid}`

- Method: `getcollabDetails`
- Response: `CollabDetailsResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Path(encoded = false, value = "todoid") | `int` | `todoid` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `helpdesk/create` [Multipart]

- Method: `getCreateTicketResponse`
- Response: `CreateTicketResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `token` |
| Part("user_id") | `RequestBody` | `user_id` |
| Part("subject") | `RequestBody` | `subject` |
| Part("description") | `RequestBody` | `description` |
| Part("type_id") | `RequestBody` | `type_id` |
| Part("sla") | `RequestBody` | `sla` |
| Part("priority_id") | `RequestBody` | `priority` |
| Part("cc") | `RequestBody` | `cc` |
| Part("dept") | `RequestBody` | `dept` |
| Part("source") | `RequestBody` | `source` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `helpdesk/create` [Multipart]

- Method: `getCreateTicketResponse`
- Response: `CreateTicketResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `token` |
| Part("user_id") | `RequestBody` | `user_id` |
| Part("subject") | `RequestBody` | `subject` |
| Part("description") | `RequestBody` | `description` |
| Part("type_id") | `RequestBody` | `type_id` |
| Part("sla") | `RequestBody` | `sla` |
| Part("priority_id") | `RequestBody` | `priority` |
| Part("cc") | `RequestBody` | `cc` |
| Part("dept") | `RequestBody` | `dept` |
| Part("source") | `RequestBody` | `source` |
| Part | `MultipartBody.Part` | `file` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `helpdesk/help-topic`

- Method: `getHelpTopicResponseNew`
- Response: `HelpTopicResponseNew`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |

## POST `helpdesk/reply` [Multipart]

- Method: `getReplyTicketResponse`
- Response: `ReplyTicketResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `token` |
| Part("ticket_id") | `RequestBody` | `ticket_id` |
| Part("reply_content") | `RequestBody` | `reply_content` |
| Part("is_reopen") | `RequestBody` | `is_reopen` |

## POST `helpdesk/reply` [Multipart]

- Method: `getReplyTicketResponse`
- Response: `ReplyTicketResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `token` |
| Part("ticket_id") | `RequestBody` | `ticket_id` |
| Part("reply_content") | `RequestBody` | `reply_content` |
| Part("is_reopen") | `RequestBody` | `is_reopen` |
| Part | `MultipartBody.Part` | `file` |

## POST `helpdesk/ticket`

- Method: `getTicketDetailResponse`
- Response: `TicketDetailResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Body | `JsonObject` | `json` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `token` |

## GET `helpdesk/tickets/1`

- Method: `getOpenTicket`
- Response: `OpenTicketResponseNew`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Query("page") | `int` | `page` |

## GET `helpdesk/tickets/4`

- Method: `getCloseTicket`
- Response: `ClosedTicketResponseNew`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Query("page") | `int` | `page` |

## GET `json`

- Method: `getAddress`
- Response: `AddressResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Query("latlng") | `String` | `latlng` |
| Query("key") | `String` | `key` |

## GET `knowledgebase/articles.php`

- Method: `getKbDetail`
- Response: `KnowledgeDetailModel`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Query("article") | `int` | `userId` |

## POST `knowledgebase/categories.php`

- Method: `getKbCategoriesResponseAsync`
- Response: `KbResponseModel`
- Parameters: none

## GET `primary-skills/get-list-api`

- Method: `getPrimarySkills`
- Response: `PrimarySkillResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Query("le1") | `String` | `client_type_id` |
| Query("le2") | `String` | `client_type_title` |
| Query("search_value") | `String` | `search_value` |

## GET `tentatives-by-category-id/{categoryid}`

- Method: `getTat`
- Response: `TatCollabResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Path(encoded = false, value = "categoryid") | `int` | `categoryid` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `todo-listing`

- Method: `getForOtherCollab`
- Response: `ForOthersCollabListingResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Query("user_type") | `Integer` | `user_type` |
| Body | `JsonObject` | `json` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `todo-listing`

- Method: `getToMeCollab`
- Response: `ToMeCollabListingResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Query("user_type") | `Integer` | `user_type` |
| Body | `JsonObject` | `json` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## GET `todos-categories`

- Method: `getCategories`
- Response: `CollabCategoriesResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Query("workflow_id") | `Integer` | `user_type` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## GET `todos-categories`

- Method: `getCategorieswithoutwid`
- Response: `CollabCategoriesResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `todos-technologies`

- Method: `getcollabtechnologies`
- Response: `TechnologyCollabResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Body | `JsonObject` | `json` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## POST `users-by-type/{categoryid}/{typeid}`

- Method: `getCollabUser`
- Response: `CollabUserSelectionResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Body | `JsonObject` | `json` |
| Path(encoded = false, value = "categoryid") | `int` | `categoryid` |
| Path(encoded = false, value = "typeid") | `int` | `typeid` |
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

## GET `workflows`

- Method: `getWorkFLows`
- Response: `CollabWorkflowResponse`
- Parameters:

| Annotation | Type | Name |
|---|---|---|
| Header(HttpHeaders.AUTHORIZATION) | `String` | `authHeader` |
| Header(HttpHeaders.ACCEPT) | `String` | `authHeaderAccept` |

