class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visits_dict = defaultdict(int)

        for d in cpdomains:
            visits, domain = d.split(" ")

            for i in range(len(domain) - 1, - 1, - 1):
                if domain[i] != ".":
                    continue
                else:
                    visits_dict[domain[i + 1:]] += int(visits)
            visits_dict[domain] += int(visits)

            solution = []
        for k in visits_dict:
            solution.append(f"{visits_dict[k]} {k}")

        return(solution)