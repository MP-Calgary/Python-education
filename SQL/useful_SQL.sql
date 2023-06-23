select * from ward_info where Birth_Date > datetime('2000-01-19');

select * from ward_info where Birth_Date > datetime('2000-01-19') and Birth_Date < datetime('2004-01-19')

SELECT "'" || Callings || "'" AS Formatted_Callings FROM ward_info;  /* Note before doing the import, did a TRIM on the columns 'Callings'

SELECT * FROM ward_info where Callings != "";
