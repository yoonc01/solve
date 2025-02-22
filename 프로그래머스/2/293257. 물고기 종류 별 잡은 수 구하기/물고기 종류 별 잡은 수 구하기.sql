SELECT COUNT(*) AS FISH_COUNT, n.FISH_NAME
FROM FISH_INFO f
JOIN
    FISH_NAME_INFO n
ON f.FISH_TYPE = n.FISH_TYPE
GROUP BY n.FISH_TYPE, n.FISH_NAME
ORDER BY COUNT(*) DESC;
