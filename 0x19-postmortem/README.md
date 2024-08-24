# Issue Summary:

* Duration of the outage: 2 hours, from 19:00 to 21:00 (UTC) on August 10, 2024

* Impact: User authentication service was down and 70% of users were unable to access their accounts on our platform. 

* Root Cause: a misconfiguration in database connection pool that happened in the latest deployment.

# Timeline:

* 19:00 (UTC): Issue detected through monitoring alert showing a spike in failed login attempts..

* Actions Taken: Engineering team  began investigation for potential causes, initially focusing on recent deployment of code.

* Misleading Investigation: The initial investigation led to considering a Distributed Denial-of-Service (DDoS) attack due to high volume of requests.

* 20:00 (UTC): After an hour of investigation, the initial assumption was eliminated and focus was shifed to backend services.

* 20:30 (UTC): The development team identified that the issue was database-related and pointed to connection configuration.

* 20:45 (UTC): Code implementation was fixed and tested.

* 21:00 (UTC): The issue was resolved and users becam able to log into their accounts..

# Root Cause and Resolution:

* Root Cause: The flash sale generated an unexpected surge in traffic, causing the web servers to become overloaded.

* Resolution: Increasing server capacity helped handle the traffic, but long-term solutions were discussed.

# Corrective and Preventative Measures:

* Improve deployment procedures:
  - Implement stricter code review processes for configuration changes
  - Add pre-deployment checklist including verification of critical settings

* Enhance monitoring and alerting:
  - Set up alerts for database connection pool utilization
  - Implement more granular monitoring of authentication service performance

* Strengthen testing:
  - Develop and run load tests simulating peak traffic conditions before each deployment
  - Implement automated tests to verify critical configuration parameters

* Documentation and knowledge sharing:
  - Create comprehensive documentation for database connection pool best practices
  - Conduct a knowledge-sharing session on the incident and lessons learned

* Incident response improvements:
  - Develop a clear escalation process for authentication-related issues
  - Create runbooks for common authentication service problems

# TODO List:

* Update deployment scripts to include configuration validation steps.

* Configure new alerts in our monitoring system for database connection pool metrics.

* Develop and implement new load testing scenarios.

* Create documentation on database connection pool configuration best practices.

* Schedule a team-wide knowledge-sharing session about the incident.

* Draft and distribute new runbooks for authentication service troubleshooting.
