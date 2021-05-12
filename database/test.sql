MERGE `temp` t
USING `authors_in_group` s
ON (t.author_group_id = ag.author_group_id)
WHEN MATCHED
THEN UPDATE SET
t.order_index = ag.order_index
WHEN NOT MATCHED BY TARGET 
THEN INSERT (`author_id`, `author_group_id`, `order_index`)
VALUES (`ag`.`author_id`, `ag`.`author_group_id`, `order_index`)
WHEN NOT MATCHED BY SOURCE
THEN DELETE;

