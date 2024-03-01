SELECT * FROM friendships

ALTER TABLE friendships ADD friendRequestStatus VARCHAR(15)
	
UPDATE friendships SET friendRequestStatus = 'ACCEPTED'