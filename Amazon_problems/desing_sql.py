from typing import List


class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.row_count_for_tables = {}
        self.table_map = {}
        for table_name in names:
            self.row_count_for_tables[table_name] = 0

    def insertRow(self, name: str, row: List[str]) -> None:
        self.row_count_for_tables[name] += 1
        row_id = self.row_count_for_tables[name]
        self.table_map[(name, row_id)] = row

    def deleteRow(self, name: str, rowId: int) -> None:
        del self.table_map[(name, rowId)]

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.table_map[(name, rowId)][columnId-1]


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)

"""
https://leetcode.com/problems/design-sql/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
Example 1:

Input
["SQL", "insertRow", "selectCell", "insertRow", "deleteRow", "selectCell"]
[[["one", "two", "three"], [2, 3, 1]], ["two", ["first", "second", "third"]], ["two", 1, 3], ["two", ["fourth", "fifth", "sixth"]], ["two", 1], ["two", 2, 2]]
Output
[null, null, "third", null, null, "fifth"]
"""