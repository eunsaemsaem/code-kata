# 재구매한 회원 ID와 재구매한 상품 ID
# 회원 ID를 기준으로 오름차순 / 상품 ID를 기준으로 내림차순

SELECT USER_ID, 
       PRODUCT_ID
FROM ONLINE_SALE 
GROUP BY USER_ID, PRODUCT_ID #회원 ID와 상품 ID를 그룹화해서
HAVING COUNT(*) >= 2         # 2개 이상인 것만
ORDER BY USER_ID, PRODUCT_ID DESC