
-- EXPLAIN ANALYZE
-- select bomb_damage_assessment, count(target_country) from mission
-- where bomb_damage_assessment is not null
-- and airborne_aircraft > 5
-- group by target_country, bomb_damage_assessment
-- order by count(bomb_damage_assessment) desc;



-- EXPLAIN ANALYZE
-- SELECT air_force, target_city, COUNT(air_force) AS mission_count
-- FROM mission
-- WHERE EXTRACT(YEAR FROM mission_date) = 1943
-- GROUP BY air_force, target_city
-- ORDER BY mission_count DESC
-- limit 1;


