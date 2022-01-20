-- 코드를 입력하세요
SET @h=-1;
SELECT @h:=@h+1 as 'HOUR', (
    SELECT COUNT(*) FROM ANIMAL_OUTS
    WHERE @h=hour(DATETIME)
) as 'COUNT' FROM ANIMAL_OUTS
WHERE @h<23;

