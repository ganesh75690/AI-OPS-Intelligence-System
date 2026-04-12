import random
from typing import Dict, List

class IncidentDetector:
    """Real-time incident detection system"""
    
    def __init__(self):
        self.events = [
            "HIGH_CPU_USAGE",
            "MEMORY_LEAK", 
            "SERVICE_FAILURE",
            "TRAFFIC_SPIKE",
            "DISK_SPACE_FULL",
            "NETWORK_LATENCY",
            "DATABASE_TIMEOUT"
        ]
        self.active_incidents = []
        
    def detect_incident(self) -> str:
        """Detect and return a random incident event"""
        event = random.choice(self.events)
        self.active_incidents.append(event)
        print(f"[EVENT DETECTED] {event}", flush=True)
        return event
    
    def get_active_incidents(self) -> List[str]:
        """Get list of active incidents"""
        return self.active_incidents
    
    def resolve_incident(self, incident: str):
        """Mark incident as resolved"""
        if incident in self.active_incidents:
            self.active_incidents.remove(incident)

class AIDecisionEngine:
    """AI-powered decision making for incident response"""
    
    def __init__(self):
        self.decision_history = []
        
    def evaluate_incident(self, event: str) -> str:
        """Evaluate incident and determine action"""
        print("[AI_DECISION] Evaluating system state...", flush=True)
        
        action_map = {
            "HIGH_CPU_USAGE": "scale_up_resources",
            "MEMORY_LEAK": "restart_service", 
            "SERVICE_FAILURE": "trigger_recovery",
            "TRAFFIC_SPIKE": "load_balance",
            "DISK_SPACE_FULL": "cleanup_storage",
            "NETWORK_LATENCY": "optimize_routing",
            "DATABASE_TIMEOUT": "restart_database"
        }
        
        action = action_map.get(event, "monitor_system")
        self.decision_history.append({"event": event, "action": action})
        
        print(f"[ACTION] {action}", flush=True)
        return action

class NotificationSystem:
    """Real-time notification system for incidents"""
    
    def __init__(self):
        self.notifications = []
        
    def notify(self, message: str, severity: str = "INFO"):
        """Send notification with severity level"""
        notification = f"[NOTIFICATION] {message}"
        self.notifications.append(notification)
        print(notification, flush=True)
        
    def notify_incident_resolved(self, incident: str, action: str):
        """Notify when incident is resolved"""
        self.notify(f"Incident '{incident}' resolved with action: {action}", "SUCCESS")
        
    def get_notifications(self) -> List[str]:
        """Get all notifications"""
        return self.notifications

class MetricsSimulator:
    """System metrics simulation for monitoring"""
    
    def __init__(self):
        self.metrics_history = []
        
    def generate_metrics(self, incident: str = None) -> Dict[str, float]:
        """Generate realistic system metrics"""
        if incident == "HIGH_CPU_USAGE":
            cpu = random.uniform(85, 95)
            memory = random.uniform(60, 80)
            status = "CRITICAL"
        elif incident == "MEMORY_LEAK":
            cpu = random.uniform(70, 85)
            memory = random.uniform(85, 95)
            status = "CRITICAL"
        elif incident == "SERVICE_FAILURE":
            cpu = random.uniform(40, 60)
            memory = random.uniform(50, 70)
            status = "WARNING"
        elif incident == "TRAFFIC_SPIKE":
            cpu = random.uniform(75, 90)
            memory = random.uniform(65, 85)
            status = "WARNING"
        else:
            cpu = random.uniform(20, 60)
            memory = random.uniform(30, 70)
            status = "HEALTHY"
            
        metrics = {
            "cpu": round(cpu, 1),
            "memory": round(memory, 1),
            "disk": random.uniform(30, 90),
            "network": random.uniform(10, 100),
            "status": status
        }
        
        self.metrics_history.append(metrics)
        
        # Print metrics in required format
        print(f"[METRICS] CPU={metrics['cpu']}% MEMORY={metrics['memory']}% STATUS={status}", flush=True)
        
        return metrics
    
    def get_metrics_history(self) -> List[Dict]:
        """Get historical metrics"""
        return self.metrics_history

class IncidentManager:
    """Main incident management system"""
    
    def __init__(self):
        self.detector = IncidentDetector()
        self.ai_engine = AIDecisionEngine()
        self.notifications = NotificationSystem()
        self.metrics = MetricsSimulator()
        
    def handle_incident_cycle(self):
        """Complete incident detection and resolution cycle"""
        # 1. Detect incident
        incident = self.detector.detect_incident()
        
        # 2. Generate metrics
        self.metrics.generate_metrics(incident)
        
        # 3. AI decision
        action = self.ai_engine.evaluate_incident(incident)
        
        # 4. Notify
        self.notifications.notify("Incident detected and handled by AI Ops system", "CRITICAL")
        
        # 5. Simulate resolution
        self.detector.resolve_incident(incident)
        self.notifications.notify_incident_resolved(incident, action)
        
        # 6. Recovery metrics
        recovery_metrics = self.metrics.generate_metrics()
        
        return {
            "incident": incident,
            "action": action,
            "metrics_before": self.metrics.metrics_history[-2] if len(self.metrics.metrics_history) >= 2 else None,
            "metrics_after": recovery_metrics,
            "notifications": self.notifications.get_notifications()[-2:]  # Last 2 notifications
        }
