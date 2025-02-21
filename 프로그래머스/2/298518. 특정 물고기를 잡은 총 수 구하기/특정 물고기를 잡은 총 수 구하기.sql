SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO fi
JOIN FISH_NAME_INFO fni
ON fi.FISH_TYPE = fni.FISH_TYPE
WHERE FISH_NAME IN ('BASS', 'SNAPPER');