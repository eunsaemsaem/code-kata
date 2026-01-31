# 2022년 10월 작성된 게시글
# 게시글 제목, 게시글 ID, 댓글 ID, 댓글 작성자 ID, 댓글 내용, 댓글 작성일
# 댓글 작성일을 기준으로 오름차순 정렬
# 댓글 작성일이 같다면 게시글 제목을 기준으로 오름차순 정렬

SELECT b.TITLE, b.BOARD_ID, r.REPLY_ID, r.WRITER_ID, r.CONTENTS, DATE_FORMAT(r.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
FROM USED_GOODS_BOARD b
    INNER JOIN USED_GOODS_REPLY r
    ON b.BOARD_ID = r.BOARD_ID
WHERE year(b.CREATED_DATE) = 2022 and month(b.CREATED_DATE) = 10
ORDER BY r.CREATED_DATE ASC, b.TITLE ASC