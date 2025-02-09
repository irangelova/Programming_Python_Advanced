from collections import deque

suggested_links = deque(int(x) for x in input().split())
featured_articles = [int(x) for x in input().split()]
target_engagement_value = int(input())
final_feed_collection = []

while suggested_links and featured_articles:
    current_suggested_link = suggested_links.popleft()
    current_featured_article = featured_articles.pop()
    if current_suggested_link == current_featured_article:
        final_feed_collection.append(0)
    else:
        dividend = max(current_suggested_link, current_featured_article)
        divisor = min(current_suggested_link, current_featured_article)
        remainder = dividend % divisor
        if dividend == current_featured_article:
            final_feed_collection.append(remainder)
            if remainder > 0:
                featured_articles.append(remainder * 2)
        else:
            final_feed_collection.append(-remainder)
            if remainder > 0:
                suggested_links.append(remainder * 2)

print(f"Final Feed: {', '.join(str(el) for el in final_feed_collection)}")
total_engagement_value = sum(final_feed_collection)
if total_engagement_value >= target_engagement_value:
    print(f"Goal achieved! Engagement Value: {total_engagement_value}")
else:
    print(f"Goal not achieved! Short by: {target_engagement_value - total_engagement_value}")
