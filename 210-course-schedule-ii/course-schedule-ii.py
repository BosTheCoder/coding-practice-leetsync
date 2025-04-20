class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adj list & counts
        adj_list = defaultdict(set)
        counts = {course:0 for course in range(numCourses)}
        total_dep = 0

        for course,dependency in prerequisites:
            adj_list[dependency].add(course)
            counts[course] += 1
            total_dep +=1
        
        ret = []
        # print("at the start")
        # print(adj_list)
        # print(counts)
        # print(total_dep)

        while counts:
            # choose course with 0 edges
            course = next((k for k,v in counts.items() if v==0), None)
            # print(f"chosen course {course}")
            if course is None:
                return []
            
            dependent_courses = adj_list[course]
            for dc in dependent_courses.copy():
                adj_list[course].remove(dc)
                counts[dc] -=1
                total_dep -=1
            
            ret.append(course)
            del counts[course]
        


        # print("att the end")
        # print(adj_list)
        # print(counts)
        return ret