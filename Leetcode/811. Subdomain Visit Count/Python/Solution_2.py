class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visits_dict = defaultdict(int)

        for d in cpdomains:
            visits, domain = d.split(" ")
            visits = int(visits)
            reversed_domain = list(reversed(domain.split(".")))
            
            running_subdomain = reversed_domain[0]
            visits_dict[running_subdomain] += visits
            for i in range(1, len(reversed_domain)):
                running_subdomain = reversed_domain[i] + "." + running_subdomain
                visits_dict[running_subdomain] += visits

            solution = []
        for k in visits_dict:
            solution.append(f"{visits_dict[k]} {k}")

        return(solution)