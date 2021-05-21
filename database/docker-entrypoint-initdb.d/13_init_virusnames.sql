SET @table_name = "virusname_gisaid";
SET @view_name = "view_virusname_gisaid";
CALL create_ordereddict_table(@table_name);
CALL create_ordereddict_view(@view_name, @table_name);
