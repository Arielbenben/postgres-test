# mission 1:

before indexing:

    -- EXPLAIN ANALYZE
    -- select bomb_damage_assessment, count(target_country) from mission
    -- where bomb_damage_assessment is not null
    -- and airborne_aircraft > 5
    -- group by target_country, bomb_damage_assessment
    -- order by count(bomb_damage_assessment) desc;

    EXPLAIN ANALYZE:
        Planning Time: 0.273 ms
        Execution Time: 93.323 ms

after indexing:

    -- create index idx_year on mission (EXTRACT(YEAR FROM mission_date));
    -- EXPLAIN ANALYZE
    -- select bomb_damage_assessment, count(target_country) from mission
    -- where bomb_damage_assessment is not null
    -- and airborne_aircraft > 5
    -- group by target_country, bomb_damage_assessment
    -- order by count(bomb_damage_assessment) desc;

    EXPLAIN ANALYZE:
        Planning Time: 0.164 ms
        Execution Time: 8.258 ms

    Explain: I chosed to create indexes on these columns because we are searching, filtering and counting on their
     values. By creating an index, we can shorter the execution time of the query.

    Compare Analyze:
        Planing Time: before - 0.273 ms, after - 0.164 ms
        Execution Time: before - 93.323 ms, after - 8.258 ms

------------------------------------------------------------------------------------------------------------------------

# mission 2:

    before indexing:

        -- EXPLAIN ANALYZE
        -- select bomb_damage_assessment, count(target_country) from mission
        -- where bomb_damage_assessment is not null
        -- and airborne_aircraft > 5
        -- group by target_country, bomb_damage_assessment
        -- order by count(bomb_damage_assessment) desc;

    EXPLAIN ANALYZE:
        Planning Time: 0.214 ms
        Execution Time: 61.372 ms

    after indexing:

        -- create index idx_bomb on mission (bomb_damage_assessment);
        -- create index idx_airborne on mission (airborne_aircraft);
        -- EXPLAIN ANALYZE
        -- select bomb_damage_assessment, count(target_country) from mission
        -- where bomb_damage_assessment is not null
        -- and airborne_aircraft > 5
        -- group by target_country, bomb_damage_assessment
        -- order by count(bomb_damage_assessment) desc;

    EXPLAIN ANALYZE:
        Planning Time: 0.202 ms
        Execution Time: 0.162 ms

    Explain: I chosed to create indexes on these columns because we are searching, filtering or counting on their
     values. By creating an index, we can shorter the execution time of the query.

    Compare Analyze:
        Planing Time: before - 0.214 ms, after - 0.202 ms
        Execution Time: before - 61.372 ms, after - 0.162 ms
