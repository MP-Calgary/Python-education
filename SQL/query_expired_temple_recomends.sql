SELECT ID, Preferred_Name, Unit_Abbreviation,
       strftime('%Y-%m-%d', 
                SUBSTR(Temple_Recommend_Expiration_Date, 5, 4) || '-' ||
                CASE SUBSTR(Temple_Recommend_Expiration_Date, 1, 3)
                    WHEN 'Jan' THEN '01'
                    WHEN 'Feb' THEN '02'
                    WHEN 'Mar' THEN '03'
                    WHEN 'Apr' THEN '04'
                    WHEN 'May' THEN '05'
                    WHEN 'Jun' THEN '06'
                    WHEN 'Jul' THEN '07'
                    WHEN 'Aug' THEN '08'
                    WHEN 'Sep' THEN '09'
                    WHEN 'Oct' THEN '10'
                    WHEN 'Nov' THEN '11'
                    WHEN 'Dec' THEN '12'
                END || '-01', 
                '+1 month', 
                '-1 day') AS Temple_Expiry_Date
FROM ward_info where Temple_Expiry_Date BETWEEN Date('now') AND Date('now','+30 days')

SELECT ID, Preferred_Name, Unit_Abbreviation,
       strftime('%Y-%m-%d', 
                SUBSTR(Temple_Recommend_Expiration_Date, 5, 4) || '-' ||
                CASE SUBSTR(Temple_Recommend_Expiration_Date, 1, 3)
                    WHEN 'Jan' THEN '01'
                    WHEN 'Feb' THEN '02'
                    WHEN 'Mar' THEN '03'
                    WHEN 'Apr' THEN '04'
                    WHEN 'May' THEN '05'
                    WHEN 'Jun' THEN '06'
                    WHEN 'Jul' THEN '07'
                    WHEN 'Aug' THEN '08'
                    WHEN 'Sep' THEN '09'
                    WHEN 'Oct' THEN '10'
                    WHEN 'Nov' THEN '11'
                    WHEN 'Dec' THEN '12'
                END || '-01', 
                '+1 month', 
                '-1 day') AS Temple_Expiry_Date
FROM ward_info where Temple_Expiry_Date BETWEEN '2024-01-1' and '2024-01-31';

SELECT ID, Preferred_Name, Unit_Abbreviation,
       strftime('%Y-%m-%d', 
                SUBSTR(Temple_Recommend_Expiration_Date, 5, 4) || '-' ||
                CASE SUBSTR(Temple_Recommend_Expiration_Date, 1, 3)
                    WHEN 'Jan' THEN '01'
                    WHEN 'Feb' THEN '02'
                    WHEN 'Mar' THEN '03'
                    WHEN 'Apr' THEN '04'
                    WHEN 'May' THEN '05'
                    WHEN 'Jun' THEN '06'
                    WHEN 'Jul' THEN '07'
                    WHEN 'Aug' THEN '08'
                    WHEN 'Sep' THEN '09'
                    WHEN 'Oct' THEN '10'
                    WHEN 'Nov' THEN '11'
                    WHEN 'Dec' THEN '12'
                END || '-01', 
                '+1 month', 
                '-1 day') AS Temple_Expiry_Date
FROM ward_info where Temple_Expiry_Date < Date('now');